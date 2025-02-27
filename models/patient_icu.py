from odoo import fields,models

class PatientIcu(models.Model):
    _name="patienticu.information"

    registration_id=fields.Many2one("administrative.data",string="Registration Code")
    admitted_date=fields.Datetime("ICU Admission")
    discharged=fields.Boolean("Discharged")
    admitted=fields.Boolean("Admitted")
    duration=fields.Integer("Boolean")
    ventilator=fields.Many2many("mechanical.ventilator")

class MechanicalVentilator(models.Model):
    _name="mechanical.ventilator"
    current=fields.Boolean("Current")
    admit_date=fields.Datetime("From")
    duration=fields.Integer("Duration")
    admit_type=fields.Integer("Type")
    remark=fields.Text("Remark")