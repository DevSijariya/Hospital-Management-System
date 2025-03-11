"""
Contains Prescription for the patient 
"""
from odoo import fields, models

class PrescriptionData(models.Model):
    """
    Contains Fields for the prescribtion model useb by the medication model by many2many fields 
    """
    _name="presecrition.data"
    _description="Contain the Prescription Information"

    print_value=fields.Boolean("Print")
    medicant_medicine=fields.Many2one('medicant.list',string="Medicament",required=True)
    indication=fields.Char("Indication",required=True)
    dose=fields.Float("Dose",required=True)
    dose_unit=fields.Selection([('mg','mg'),('g','g')])
    form=fields.Char("Form")
    frequency=fields.Integer("Frequency",required=True)
    quantity=fields.Integer("Quantity",required=True)
    treatment_duration=fields.Integer("Treatment Duration",required=True)
    treatment_period=fields.Selection([('days','Days'),('months','Months')],required=True)
    allow_substitution=fields.Boolean("Allow Substitution")
    comment=fields.Text("Comment")
