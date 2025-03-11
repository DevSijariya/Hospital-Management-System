from odoo import fields,models,api

class NursingModel(models.Model):
    _name="nursing.description"

    name=fields.Char("Name",required=True)
    health_profession=fields.Char("Health Professional")
    base_condition=fields.Char("Base Condition")
    session=fields.Integer("Session")
    ordering_physician_name=fields.Many2one('doctors.data')
    patient=fields.Many2one("patients.description",required=True)
    related_evaluation=fields.Char("Related Evaluation")
    start=fields.Datetime("Start")
    procedure=fields.One2many('procedure.information','nursing_id')
    
    @api.constrains('patient')
    def _update_test_details(self):
        for record in self:
            if record.patient:
                patient_info = self.env['patients.description'].search([('id', '=', record.patient.id)], limit=1)
                if patient_info:
                    record.health_profession = patient_info.primary_doctor.name


class Procedures(models.Model):
    _name="procedure.information"

    code=fields.Char("Code")
    comment=fields.Text("Comment")
    nursing_id=fields.Many2one('nursing.description')