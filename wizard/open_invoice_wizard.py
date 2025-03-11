from odoo import fields,models

class OpenInvoiceWizards(models.TransientModel):
    _name="openinvoice.wizard"
    medical_id=fields.Many2one('medical.service')
    def open_invoice(self):
        return {
            "name": "create invoice",
            "type": "ir.actions.act_window",
            "res_model": "account.move",
            "view_mode":"form",
            "res_id":False,
            "context":{'default_move_type':'out_invoice'}
        }

class CreateShipmentWizards(models.TransientModel):
    _name="shipment.wizard"


    def open_invoice(self):
        pass

class OpenlabtestWizards(models.TransientModel):
    _name="openlabtest.wizard"
    _description=" Delete Teachers Data"

    def create_request(self):
        return {
            "name": "Create Lab Test",
            "type": "ir.actions.act_window",
            "res_model": "labtest.information",
            "views": [[False, "list",'form']],
        }