"""
    Contains Beds Data which can be used in the patient class 
"""
from odoo import fields,models

class BedDetails(models.Model):
    """
        Only name field in define to used by the patient to occupy the bed only one bed is allocate to one patient at a time
    """
    _name="beddetails.information"

    name=fields.Char("Bed Number",required=True)
    ward=fields.Many2one('healthcenter.ward',required=True)
    status=fields.Selection([('free','Free'),('occupied','Occupied')])
    


class NumberData(models.Model):
    _name="number.data"
    _rec_name="value"
    value=fields.Char('Number')