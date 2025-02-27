from odoo import fields, models

class LabTestModel(models.Model):
    _name="lab.test"
    _description="Contains the lab result of the patient"

    blood_type=fields.Selection([('A','A'),('AB','AB'),('O','O'),('B','B')])
    rh_value=fields.Selection([('+','+'),('-','-')])
    ethnic_group=fields.Selection([('general','General'),('Asian','Asian'),('African','African'),('African American','African American')])
    insurance_company_name=fields.Char("Insaurance Company Name")
    family=fields.Char("Family")
    recievable=fields.Integer("Recievable")
    primary_doctor=fields.Char("Primary Care Doctor")