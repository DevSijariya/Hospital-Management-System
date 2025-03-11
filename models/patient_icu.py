"""
This file contains the model of the icu to save the record of the patient icu history
"""
from odoo import fields,models,api
from odoo.exceptions import UserError,ValidationError


class PatientIcu(models.Model):
    """
    This Class contains the fields of the Patient Icu record
    """
    _name="patienticu.information"
    _rec_name="registration_id"

    registration_id=fields.Many2one("administrative.data",string="Registration Code",required=True)
    admitted_date=fields.Datetime("ICU Admission",required=True)
    discharged=fields.Boolean("Discharged",required=True)
    admitted=fields.Boolean("Admitted")
    duration=fields.Integer("Boolean")
    ventilator=fields.Many2many("mechanical.ventilator")

    @api.constrains('discharged')
    def validate_values(self):
        if self.discharged and self.admitted:
            raise UserError("Admitted and discharged both are not true at the same time")
        if not self.discharged and not self.admitted:
            raise UserError("Admitted and discharged both are not false at the same time")

class MechanicalVentilator(models.Model):
    """
    This Model Contains the record of the patiet Ventilator history
    """
    _name="mechanical.ventilator"
    current=fields.Boolean("Current")
    admit_date=fields.Datetime("From",required=True)
    duration=fields.Integer("Duration")
    admit_type=fields.Integer("Type",required=True)
    remark=fields.Text("Remark")

