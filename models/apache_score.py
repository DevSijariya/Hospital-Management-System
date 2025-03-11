"""
    Apache Score file is contains the apache information of the patients it contains class and fields respectively
"""

from odoo import fields, models,api

class ApacheScore(models.Model):
    """
        Apache Score fields and methods is define
    """
    _name="apache2.score"
    _description="Creating the Apache Score Form For the patient"
    _rec_name="registration_code"

    registration_code=fields.Many2one("administrative.data",string="Registration Code")
    age=fields.Integer("Age")
    result_date=fields.Datetime("Date")
    temperature=fields.Float("Temperature")
    heart_rate=fields.Float("Heart Rate")
    fio2=fields.Float("Fio2")
    paco2=fields.Float("PaCO2")
    ph_value=fields.Float("pH")
    potassium=fields.Float("Potassium")
    hemacocrait=fields.Float("Hematcocrit")
    arf=fields.Boolean("ARF")
    map=fields.Integer("MAP")
    respiratory_rate=fields.Integer("Respiratory Rate")
    pao2=fields.Integer("PaO2")
    ado2=fields.Integer("A-a DO2")
    sodium=fields.Integer("sodium")
    creatitine=fields.Float("Creatinine")
    wbc=fields.Float("WBC")
    chronic_condition=fields.Boolean("Chronic Condition")
    score=fields.Float("Score")

    @api.constrains('registration_code')
    def find_age(self):
        patient_age=self.registration_code.patient_id.age
        self.age=patient_age