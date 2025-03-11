"""
This File Contains the Administratinve form class and functions
"""
from odoo import fields,models,api
from odoo.exceptions import UserError,ValidationError

class AdministrativeData(models.Model):
    """
    Description : This Class is used to create the administrative Model
    """
    _name="administrative.data"
    _description="Creating the administration panel"
    _rec_name="registration_code"

    registration_code=fields.Char("Registration Code")
    patient_id=fields.Many2one(comodel_name="patients.description",required=True)
    hospital_bed=fields.Char("Bed")
    hospitalization_date=fields.Datetime("Hospitalization Date",required=True)
    expected_discharge=fields.Datetime("Expected Discharge",required=True)
    attending_physician_name=fields.Char("Attending Physician")
    operating_physician=fields.Many2one('doctors.data',required=True)
    admission_type=fields.Selection([('Not Urgent','Non Serious'),('Urgent','Serious'),('veryUrgent','Critical')],required=True)
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

    @api.onchange('patient_id')
    def _onchange_user_id(self):
        """
            Update the user information and update the info based on the changes in patient id
        """
        for record in self:
            if record.patient_id:
                record.attending_physician_name=record.patient_id.primary_doctor.name
            else:
                record.attending_physician_name=False

    @api.constrains('hospitalization_date')
    def validate_date(self):
        """
        Validate the admitted date 
        """
        for record in self:
            if record.hospitalization_date>record.expected_discharge:
                raise UserError("Discharge Date must be greater than Admitted date")

    @api.constrains('patient_id')
    def _onchange_patient_id(self):
        """
        Auto-fill the hospital_bed field based on the selected patient's bed_occupied field
        """
        if self.patient_id:
            self.hospital_bed = self.patient_id.bed_taken.name
        else:
            self.hospital_bed = False
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
        
        related_recordset = self.env["bed.info"].search([('patient_id.id','=',self.patient_id.id)])
        self.transfer_bed = related_recordset


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
           'state': "ongoing",
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
    
