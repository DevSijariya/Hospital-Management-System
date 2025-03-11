"""
This File is used to create the ECG Model
"""
from odoo import fields,models

class EcgModel(models.Model):
    """
    Contain ECG Fields
    """
    _name="ecg.information"
    _rec_name="registration_code"

    registration_code=fields.Many2one("administrative.data",string="Registration Code",required=True)
    admit_date=fields.Datetime("Date",required=True)
    axis=fields.Char("Axis")
    rate=fields.Integer("Rate")
    pacemaker=fields.Selection([('applied','Applied'),('Not Applied','Not Applied')],required=True)
    rhythm=fields.Selection([('regular','Regular'),('not regular','Not Regular')])
    pr=fields.Integer("Pr")
    qrs=fields.Integer("QRS")
    qt=fields.Integer("QT")
    st_segment=fields.Selection([('Normal','Normal'),('Abnormal','Abnormal')],required=True)
    twave=fields.Boolean("T Wave Inversion")
    interpretation=fields.Selection([('No','No'),('Yes','Yes')])

class GscModel(models.Model):
    """
    This Class Contains the CSC Fields
    """
    _name="gscmodel.information"
    _rec_name="registration_code"

    registration_code=fields.Many2one("administrative.data",string="Registration Code",required=True)
    admit_date=fields.Datetime("Date",required=True)
    eyes=fields.Selection([('Do not open eyes','Do not open eyes'),('open eyes normal','open eyes and normal'),('open eyes but damaged','open eyes but damaged')],required=True)
    verbal=fields.Char('Verbal')
    motor=fields.Char('Motor')
    glasgow=fields.Char('Glasgow')
