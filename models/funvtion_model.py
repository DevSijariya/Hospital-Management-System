from odoo import fields,models

class MainModel(models.Model):
    _name="model.model"

    name=fields.Char('Name')

class FunctionModel(models.Model):
    _name="function.function"

    name=fields.Char('Name')
    model_ids=fields.Many2many("model.model",string="Model id")

    def update_data(self):
        return {
            "name": "Update Wizard",
            "type": "ir.actions.act_window",
            "res_model": "openupdate.wizard",
            "view_mode":"form",
            "target":"new",
        }