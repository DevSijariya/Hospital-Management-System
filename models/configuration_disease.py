from odoo import fields,models,api

class PathologyGroups(models.Model):
    _name="pathology.groups"
    name=fields.Char("Name",required=True)
    code=fields.Char("Code")
    description=fields.Text("Short Description")
    
    @api.constrains('name')
    def genrate_code(self):
        self.code= self.env['ir.sequence'].next_by_code('pathology.id')


class Disease(models.Model):
    _name="disease.groups"
    name=fields.Char("Name",required=True)
    code=fields.Char("Code")
    categeory=fields.Many2one('disease.categeory',string="Disease Categeory")

    @api.constrains('name')
    def genrate_code(self):
        self.code= self.env['ir.sequence'].next_by_code('disease.id')

class DiseaseCategeory(models.Model):
    _name="disease.categeory"
    name=fields.Char("Name")

class MedicalProcedure(models.Model):
    _name="medical.procedure"
    name=fields.Char("Code")
    description=fields.Text("Long Text")
    