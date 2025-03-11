"""
Appointment Model Contain the fields of appointment
"""
from odoo import fields, models,api
from odoo.exceptions import UserError

class AppointmentDetail(models.Model):
    """
    Appointment Class
    """
    _name="appointment.data"
    _description="Used to Provide the appointment of the patients"
    _rec_name="appointment_id"
    
    appointment_id=fields.Char("Appointment Id",readonly=True)
    physician_name=fields.Char('Physician',readonly=True)
    speciality=fields.Char("Speciality")
    appointment_start=fields.Datetime("Appointment Date",required=True)
    appointment_end=fields.Datetime("Appointment End",required=True)
    patient_status=fields.Selection([('Outpatient','Outpatient'),('Inpatient','Inpatient')])
    invoice_exempt=fields.Boolean("Invoice exempt")
    status=fields.Selection([('invoiced','To be Invoiced'),('uninvoiced','Not to be Invoinced')])
    validity_date=fields.Datetime("Validity Date",required=True)
    health_center=fields.Many2one('healthcenter.building',string="Health Center")
    duration=fields.Integer("Duration")
    urgency_level=fields.Selection([('Not Urgent','Non Serious'),('Urgent','Serious'),('veryUrgent','Critical')],readonly=True)
    invoice_to_insurace=fields.Boolean("Invoice to Insurance")
    consultiation_service=fields.Selection([('consulting','Consulting'),('notconsulting','Not Consulting')])
    comment=fields.Text("Comment")
    patient_id=fields.Many2one(comodel_name="patients.description",required=True)


    def downlaod_appointment_letter(self):
        """
        This Duntion triggers the qweb report to download the pdf
        """
        return self.env.ref("hospital_management_system.action_report_patient_appointment_template").report_action(self)

    def open_wizard_invoice(self):
        """
        Calling the Wizards using the button
        """
        return {
                "name":"Save Precautions",
                "type": "ir.actions.act_window",
                "res_model": "openinvoice.wizard",
                "views": [[False, "form"]],
                "target": "new",
        }
    @api.constrains('patient_id')
    def _onchange_user_id(self):
        """
            Update the user information and update the info based on the changes in patient id
        """
        for record in self:
            if record.patient_id:
                record.physician_name=record.patient_id.primary_doctor.name
                physician_id=self.env['physician.proffesional.info'].search([('name','=',record.physician_name)],limit=1)
                record.speciality=physician_id.speciality
            else:
                record.physician_name=False


    @api.model
    def create(self, vals):
        """
        Create the record and assignt the unique id
        """
        vals['appointment_id']=self.env['ir.sequence'].next_by_code('appointment.registratin.id')
        result = super(AppointmentDetail, self).create(vals)
        return result

    @api.constrains('appointment_end')
    def validate_date(self):
        for record in self:
            if record.appointment_start>record.appointment_end:
                raise UserError("Appointment End Date must be less than start date")