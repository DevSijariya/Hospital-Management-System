from odoo import fields,models

class OpenInvoiceWizards(models.TransientModel):
    _name="openupdate.wizard"


    model_ids=fields.Many2many("model.model",string="Model Id")

    def update_data(self):
        ids=self._context['active_ids']
        # import pdb;pdb.set_trace()
        id_value=[value for value in self.model_ids.id]
        for id in ids:
            record=self.env['function.function'].browse(id)
            if self.model_ids:
                record.write({
                    "model_ids":[(4, value) for value in id_value]
                })