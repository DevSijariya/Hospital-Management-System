"""
Appointment Model Contain the fields of appointment
"""
from odoo import fields, models,api

class AppointmentDetail(models.Model):
    """
    Appointment Class
    """
    _name="appointment.data"
    _description="Used to Provide the appointment of the patients"
    _rec_name="appointment_id"
    appointment_id=fields.Char("Appointment Id",readonly=True)
    physician=fields.Many2one('res.partner')
    speciality=fields.Char("Speciality")
    appointment_start=fields.Datetime("Appointment Date")
    appointment_end=fields.Datetime("Appointment End")
    patient_status=fields.Selection([('Outpatient','Outpatient'),('Inpatient','Inpatient')])
    invoice_exempt=fields.Boolean("Invoice exempt")
    status=fields.Selection([('invoiced','To be Invoiced'),('uninvoiced','Not to be Invoinced')])
    validity_date=fields.Datetime("Validity Date")
    health_center=fields.Char("Health Center")
    duration=fields.Integer("Duration")
    urgency_level=fields.Selection([('Not Urgent','Non Serious'),('Urgent','Serious'),('veryUrgent','Critical')])
    invoice_to_insurace=fields.Boolean("Invoice to Insurance")
    consultiation_service=fields.Selection([('consulting','Consulting'),('notconsulting','Not Consulting')])
    comment=fields.Text("Comment")
    patient_id=fields.Many2one(comodel_name="patients.description")


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

    @api.model
    def create(self, vals):
        """
        Create the record and assignt the unique id
        """
        vals['appointment_id']=self.env['ir.sequence'].next_by_code('appointment.registratin.id')
        result = super(AppointmentDetail, self).create(vals)
        return result
