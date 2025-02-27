from odoo import fields, models

class PrescriptionData(models.Model):
    _name="presecrition.data"
    _description="Contain the Prescription Information"

    print_value=fields.Boolean("Print")
    medicant=fields.Char("Medicament")
    indication=fields.Char("Indication")
    dose=fields.Float("Dose")
    dose_unit=fields.Selection([('mg','mg'),('g','g')])
    form=fields.Char("Form")
    frequency=fields.Integer("Frequency")
    quantity=fields.Integer("Quantity")
    treatment_duration=fields.Integer("Treatment Duration")
    treatment_period=fields.Selection([('days','Days'),('months','Months')])
    allow_substitution=fields.Boolean("Allow Substitution")
    comment=fields.Text("Comment")