from odoo import fields,models

class OpenInvoiceWizards(models.TransientModel):
    _name="openupdate.wizard"


    model_ids=fields.Many2many("model.model",string="Model Id")

    def update_data(self):
        ids=self._context['active_ids']
        for id in ids:
            record=self.env['function.function'].browse(id)
            if self.model_ids:
                record.write({
                    "model_ids":[(4, self.model_ids.id)]
                })