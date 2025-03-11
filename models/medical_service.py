from odoo import fields,models

class MedicalService(models.Model):
    _name="medical.service"

    name=fields.Char("Name")
    desription=fields.Char("Description")
    patient=fields.Many2one('patients.description',required=True)
    date=fields.Datetime("Date",required=True)
    state=fields.Selection([('draft','draft'),('confirm','confirm')],default="draft")
    product_ids=fields.Many2many('product.description')
    def confirm_button(self):
        self.state='confirm'

    def create_invoice(self):
        return {
            "name": "create invoice",
            "type": "ir.actions.act_window",
            "res_model": "openinvoice.wizard",
            "views": [[False, "form"]],
            "target": "new",
            "context":("patient.id",self.id),
        }
    def create(self,vals):
        vals['name']=self.env['ir.sequence'].next_by_code('create.medical')
        result = super(MedicalService, self).create(vals)
        return result

class ProductDescription(models.Model):
    _name="product.description"
    invoice=fields.Boolean("Invoice")
    description=fields.Char("Description")
    product=fields.Char("Product")
    quantity=fields.Integer("Qty")
    start=fields.Datetime("From")
    end=fields.Datetime("End")
