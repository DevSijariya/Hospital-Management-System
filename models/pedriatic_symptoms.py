"""
This file contaiuns the model of the pedriatric symptoms
"""
from odoo import fields ,models,api

class PedriaticSymptoms(models.Model):
    """
    Contians Fields and Methods of the model
    """
    _name="pedriatric.symptoms"
    _rec_name="patient_id"

    patient_id=fields.Many2one("patients.description")
    date=fields.Datetime("Date")
    health_professional=fields.Char("Health Professional")
    appointment_id=fields.Char("Appointment")
    pcs_total=fields.Char("Pcs Total")
    complain=fields.Selection([('never','Never'),('sometimes','Sometimes'),('Regular','Regular')],string="Complain of aches and pains")
    spend_time=fields.Selection([('never','Never'),('sometimes','Sometimes'),('Regular','Regular')],string="spend more time alone")
    little_energy=fields.Selection([('never','Never'),('sometimes','Sometimes'),('Regular','Regular')],string="Tires easily and little energy")
    fidgety=fields.Selection([('never','Never'),('sometimes','Sometimes'),('Regular','Regular')],string="Fidgety and unable to sit still")
    trouble_with_teacher=fields.Selection([('never','Never'),('sometimes','Sometimes'),('Regular','Regular')],string="Has trouble with teacher")
    school_interest=fields.Selection([('never','Never'),('sometimes','Sometimes'),('Regular','Regular')],string="Less Intersted in School")
    act_as_drivern=fields.Selection([('never','Never'),('sometimes','Sometimes'),('Regular','Regular')],string="Act as driven by motor")
    grades_drop=fields.Selection([('never','Never'),('sometimes','Sometimes'),('Regular','Regular')],string="School Grades droping")
    is_down=fields.Selection([('never','Never'),('sometimes','Sometimes'),('Regular','Regular')],string="Is down him or herself")
    visit_doctor=fields.Selection([('never','Never'),('sometimes','Sometimes'),('Regular','Regular')],string="Visit the Doctor with doctor finding")
    trouble_with_sleeping=fields.Selection([('never','Never'),('sometimes','Sometimes'),('Regular','Regular')],string="Trouble with sleeping")
    worries=fields.Selection([('never','Never'),('sometimes','Sometimes'),('Regular','Regular')],string="worries a lot")
    want_to_be=fields.Selection([('never','Never'),('sometimes','Sometimes'),('Regular','Regular')],string="Want to be with you more than before")
    feels_bad=fields.Selection([('never','Never'),('sometimes','Sometimes'),('Regular','Regular')],string="Feels he or she is bad")
    risks=fields.Selection([('never','Never'),('sometimes','Sometimes'),('Regular','Regular')],string="Takes Unnessesary risks")
    hurts=fields.Selection([('never','Never'),('sometimes','Sometimes'),('Regular','Regular')],string="Gets Hurts Often")
    remark=fields.Text("Remark")
    
    @api.onchange('patient_id')
    def _onchange_user_id(self):
        """
            Update the user information and update the info based on the changes in patient id
        """
        for record in self:
            if record.patient_id:
                record.health_professional=record.patient_id.primary_doctor.name
            else:
                record.health_professional=False

            id=self.env['appointment.data'].search([('patient_id','=',record.patient_id.id)],limit=1)
            self.appointment_id=id.appointment_id
