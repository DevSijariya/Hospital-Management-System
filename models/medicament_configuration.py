from odoo import fields,models

class MedicamentCategeory(models.Model):
    _name="medicament.categeory"

    name=fields.Char('Name',required=True)