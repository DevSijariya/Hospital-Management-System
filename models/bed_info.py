"""
Contains the Bed Information
"""
from odoo import fields, models

class BedInfo(models.Model):
    """
    This class contains the bed information which is available and occupied
    """
    _name = "bed.info"
    _description = "Contain Information about the available bed"

    patient_id = fields.Many2one(comodel_name="patients.description")
    shiftdate = fields.Datetime("Date", default=fields.Datetime.now)
    shift_from = fields.Selection([
        ('Bed 1', 'Bed 1'), ('Bed 2', 'Bed 2'),
        ('Bed 3', 'Bed 3'), ('Bed 4', 'Bed 4')
    ])
    shift_to = fields.Selection([
        ('Bed 1', 'Bed 1'), ('Bed 2', 'Bed 2'),
        ('Bed 3', 'Bed 3'), ('Bed 4', 'Bed 4')
    ])
    shift_reason = fields.Char("Reason")
    admin_id = fields.Many2one("administrative.data")
