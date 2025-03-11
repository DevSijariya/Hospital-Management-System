from odoo import fields,models

class MedicantList(models.Model):
    _name="medicant.list"

    name=fields.Char("Name",required=True)
    active_component=fields.Char('Active Component')
    categeory_medicine=fields.Many2one('medicament.categeory',string="Categeory",required=True)
    available=fields.Integer('Available Quantity',required=True)
    effect=fields.Char("Therapatic Effect")
    pregnancy_warning=fields.Char("Pregnancy Warning")
    price=fields.Integer("Price",required=True)


class PatientEvaluation(models.Model):
    _name="patient.evaluation"
    _rec_name="patient"
    patient=fields.Many2one('patients.description',required=True)
    start=fields.Datetime("Start Evalation")
    complain=fields.Datetime("Cheif Complaint")
    type_assign=fields.Char("Type")
    end=fields.Datetime("End Evaluation")
    doctor=fields.Many2one('doctors.data',string="Doctor")
    summary=fields.Text("Summary")

    def action_confirm(self):
        pass    