from odoo import fields,models

class AppointmentEvaluation(models.TransientModel):
    _name = "appintment.evaluation"
    name=fields.Char("Name of Evaluation")
    speciality=fields.Char("Speciality")
    start_date=fields.Datetime("Start Date")
    end_date=fields.Datetime("End Date")

    def appoint_eval(self):
        domain=[]
        if self.name:
            domain.append(('physician_name','=',self.name))
        if self.speciality:
            domain.append(('speciality','=',self.speciality))
        if self.start_date:
            domain.append(('appointment_start','=',self.start_date))
        if self.end_date:
            domain.append(('appointment_end','=',self.end_date))
        return {
                "name":"Appointment as per evaluation",
                "type": "ir.actions.act_window",
                "res_model": "appointment.data",
                "view_mode":"list","form"
                "domain":domain,
                "target": "new",
        }
