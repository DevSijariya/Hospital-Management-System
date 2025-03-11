from odoo import fields,models,api

class DraftLabRequst(models.Model):
    _name="draftlab.request"
    _rec_name="request"
    request=fields.Char("Request")
    test_typ=fields.Many2one('labtesting.type')
    date=fields.Datetime("Date")
    patient_id=fields.Many2one(comodel_name="patients.description",required=True)
    doctor=fields.Many2one(comodel_name="doctors.data",required=True)
    state = fields.Selection(selection=[
        ('draft', 'Draft'),
        ('cancel', 'Cancel'),
        ('done', 'Tested'),
        ], string='Status', readonly=True, copy=False,
        tracking=True, default='draft')
    
    def create_lab_test(self):
        return {
            "name": "Create Lab Test",
            "type": "ir.actions.act_window",
            "res_model": "openlabtest.wizard",
            "views": [[False, "form"]],
            "target": "new",
        }
    @api.constrains('request')
    def generate_sequence(self):
        self['request']=self.env['ir.sequence'].next_by_code('draft.request')

    
class LabTest(models.Model):
    _name="labtest.information"
    _rec_name="test_id"
    
    test_id=fields.Char("ID")
    date_of_analysis=fields.Datetime("Date of Analysis")
    doctor_name=fields.Char("Phatologist Physician")
    test_type=fields.Char("Test Type")
    patient_name=fields.Many2one(comodel_name="patients.description",required=True)
    date_requested=fields.Char("Date Requested")
    test_case=fields.One2many('testcases.result','lab_test',compute="_compute_fields")
    request=fields.Char('Request')
    diagnosis=fields.Char("Diagnosis")
    
    @api.constrains('patient_name')
    def _update_test_details(self):
        for record in self:
            if record.patient_name:
                test = self.env['draftlab.request'].search([('patient_id', '=', record.patient_name.id)], limit=1)
                if test:
                    record.test_type = test.test_typ.name
                    record.doctor_name = test.doctor.name
                    record.date_requested = test.date
    
    def create(self,vals):
        vals['test_id']=self.env['ir.sequence'].next_by_code('create.request')
        return super(LabTest,self).create(vals)
    def _compute_fields(self):
        """
        Used to get the one2many fields automatically
        """
        
        related_recordset = self.env["testcases.result"].search([('patient_id.id','=',self.patient_id.id)])
        self.test_case = related_recordset
    

class TodayDraftLabRequst(models.Model):
    _name="today.draftlab.request"
    _rec_name="request"
    request=fields.Char("Request")
    test_type=fields.Selection([('CBC','Blood Test(CBC)'),('RBC','Blood Test(RBC)')])
    date=fields.Datetime("Date")
    patient_id=fields.Many2one(comodel_name="patients.description",required=True)
    doctor=fields.Many2one(comodel_name="res.partner",required=True)
    state = fields.Selection(selection=[
        ('draft', 'Draft'),
        ('cancel', 'Cancel'),
        ('done', 'Tested'),
        ], string='Status', readonly=True, copy=False,
        tracking=True, default='draft')