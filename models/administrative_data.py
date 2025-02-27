"""
This File Contains the Administratinve form class and functions
"""
from odoo import fields,models,api
class AdministrativeData(models.Model):
    """
    Description : This Class is used to create the administrative Model
    """
    _name="administrative.data"
    _description="Creating the administration panel"
    _rec_name="registration_code"

    registration_code=fields.Char("Registration Code")
    patient_id=fields.Many2one(comodel_name="patients.description")
    hospital_bed=fields.Selection([('Bed 1','Bed 1'),('Bed 2','Bed 2'),('Bed 3','Bed 3'),('Bed 4','Bed 4')])
    hospitalization_date=fields.Datetime("Hospitalization Date")
    expected_discharge=fields.Datetime("Expected Discharge")
    attending_physician=fields.Many2one('res.partner')
    operating_physician=fields.Many2one('res.partner')
    admission_type=fields.Selection([('Not Urgent','Non Serious'),('Urgent','Serious'),('veryUrgent','Critical')])
    reason=fields.Text("Reason for Admission")
    transfer_bed=fields.One2many(comodel_name="bed.info",inverse_name="admin_id", string="Transfer Bed",compute="_compute_fields")
    state = fields.Selection(selection=[
       ('draft', 'Free'),
       ('in_progress', 'Confirmed'),
       ('cancel', 'Cancelled'),
       ('ongoing', 'Hospitalized'),
       ('done', 'Done'),
    ], string='Status', readonly=True, copy=False,
    tracking=True, default='draft')

    @api.model
    def create(self, vals):
        """
        Create the record and assign the unique id
        """
        vals['registration_code']=self.env['ir.sequence'].next_by_code('patient.registratin.id')
        result = super(AdministrativeData, self).create(vals)
        return result
    
    def _compute_fields(self):
        """
        Used to get the one2many fields automatically
        """
        related_recordset = self.env["bed.info"].search([])
        self.transfer_bed = related_recordset

    @api.onchange('patient_id')
    def _onchange_patient_id(self):
        """
        Auto-fill the hospital_bed field based on the selected patient's bed_occupied field
        """
        if self.patient_id:
            self.hospital_bed = self.patient_id.bed_occupied
        else:
            self.hospital_bed = False  

    def button_in_progress(self):
        """
        Used to change the state
        """
        self.write({
           'state': "in_progress"
        })

    def confirm_update(self):
        """
        Used to change the state
        """
        self.write({
           'state': "ongoing"
       })

    def completed(self):
        """
        Used to change the state
        """
        self.write({
           'state': "done"
       })

    def button_in_draft(self):
        """
        Used to change the state
        """
        self.write({
           'state': "draft"
       })

    def bed_transfer(self):
        """
        Open the Bed Transfer Wizard
        """
        return {
            "name": "Bed Transfer",
            "type": "ir.actions.act_window",
            "res_model": "bedtransfer.wizard",
            "views": [[False, "form"]],
            "target": "new",
        }