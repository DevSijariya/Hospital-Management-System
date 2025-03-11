from odoo import fields,models,api

class Newborn(models.Model):
    _name="newborn.description"

    name=fields.Char("Baby Name",required=True)
    image=fields.Image("image")
    newborn_id=fields.Char("Newborn Id")
    gender=fields.Selection([('Male','Male'),('female','Female')],string="Sex")
    discharged=fields.Datetime("Discharged",required=True)
    weight=fields.Integer("Weight",required=True)
    doctor=fields.Many2one("doctors.data",string="Doctor in Charge")
    mother=fields.Many2one("patients.description",required=True)
    date_of_birth=fields.Datetime("Date of birth",required=True)
    length=fields.Integer("Length",required=True)
    cephalic=fields.Integer("Cephalic Perimeter")
    apgar_score=fields.One2many("apgarscore.record",'newborn_id')
    
    @api.onchange('mother')
    def _onchange_user_id(self):
        """
            Update the user information and update the info based on the changes in patient id
        """
        for record in self:
            if record.mother:
                record.doctor=record.mother.primary_doctor.name
            else:
                record.doctor=False
    
    @api.model
    def create(self, vals):
        """
        This Function generate the sequence of the prescription id and then save the record
        """
        vals['newborn_id']=self.env['ir.sequence'].next_by_code('newborn.baby.id')
        result = super(Newborn, self).create(vals)
        return result
    
    def downlaod_card(self):
        return self.env.ref("hospital_management_system.action_report_baby_card_template").report_action(self)

class ApgarScore(models.Model):
    _name="apgarscore.record"
    minutes=fields.Integer("Minutes",required=True)
    respiratory=fields.Selection([('present','Present'),('Absent','Absent')],string="Respiratory")
    activity=fields.Char("Activity")
    appeareance=fields.Char("Appeareance")
    pulse=fields.Selection([('<100','<100'),('>100','>100')],string="Pulse",required=True)
    apgar_score=fields.Integer("Apgar Score")
    grimace=fields.Char("Grimace")
    newborn_id=fields.Many2one('newborn.description')