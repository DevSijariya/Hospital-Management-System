from odoo import fields,models

class TestCasesResult(models.Model):
    _name="testcases.result"
    _rec_name="sequence"
    sequence=fields.Char("Sequence")
    names=fields.Many2one("patients.description")
    result=fields.Char("result")
    normal_range=fields.Char("Normal Range")
    units=fields.Integer("Units")
    lab_test=fields.Many2one('labtest.information')