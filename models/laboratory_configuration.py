from odoo import fields,models,api

class LabTestingType(models.Model):
    _name="labtesting.type"
    name=fields.Char("Name")
    code=fields.Char("Code")
    @api.constrains('name')
    def genrate_code(self):
        self.code= self.env['ir.sequence'].next_by_code('test.id')


class LabTestingUnit(models.Model):
    _name="labtesting.unit"
    name=fields.Char("Name")
    code=fields.Char("Code")