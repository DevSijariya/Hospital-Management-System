from odoo import models,fields,api
from odoo.exceptions import UserError,ValidationError


class SurgeryData(models.Model):
    _name="surgery.data"

    name=fields.Many2one("patients.description",required=True)
    code=fields.Char('Code')
    description=fields.Char('Description')
    base_condition=fields.Char('Base Condition')
    surgery_classification=fields.Selection([('required','Required'),('not required','Not Required')])
    date=fields.Datetime("Date of Surgery")
    age=fields.Char("Patient Age")
    surgion=fields.Char("Surgieon")
    extra_info=fields.Text("Extra Info")

    base_urls=fields.Html('Base Url')
    number_id=fields.Many2one('number.data',string="Select Number")
    number=fields.Integer('Number')
    state=fields.Selection([('true','True'),('false','False')])


    @api.onchange('number_id')
    def check(self):
        url= self.env['patients.description'].get_base_url()
        action=self.env.ref('hospital_management_system.action_number').id
        for records in self:
            urls=f"{url}/odoo/action-{action}/new"
            records.base_urls=f'<a href="{urls}">Click Here</a>'

            if int(records.number_id.value)<1:
                records.state='true'
            else:
                records.state='false'


    @api.constrains('name')
    def get_values(self):
        nurse=self.env['nursing.description'].search([('patient','=',self.name.id)],limit=1)
        self.base_condition=nurse.base_condition
        self.surgion=nurse.health_profession
        self.code=nurse.procedure.code
        patient=self.env['patients.description'].browse(self.name.id)
        self.age=patient.age
            
    @api.model
    def create(self,vals):
        number=self.env['number.data'].browse(vals['number_id'])
        if int(number.value)>1:
            return super(SurgeryData,self).create(vals)
        else:
            raise ValidationError("Invalid")

