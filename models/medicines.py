from odoo import fields, models,api


class MedicinesDescription(models.Model):
    _name = "medicines.description"
    _description = "Medicines Description"
    _rec_name="prescription_id"

    patient_id=fields.Many2one(comodel_name="patients.description",string="Patient")
    prescription_date=fields.Datetime("Prescription Date")
    pharmacy=fields.Char("Pharmacy")
    prescription_id=fields.Char("Prescription Id")
    login_user=fields.Selection([('Administration','Administration'),('User','User')])
    prescribing_doctor=fields.Char("Prescribing Doctor")
    invoice_insurance=fields.Boolean("Invoive to Insurance")
    prescription_data=fields.Many2many('presecrition.data',string="Prescribe Medicines")

    notes=fields.Text("Notes")


    @api.model
    def create(self, vals):
        vals['prescription_id']=self.env['ir.sequence'].next_by_code('patient.prescription.id')
        result = super(MedicinesDescription, self).create(vals)
        return result
    
    def create_shipment(self):
        """
        Calling the Wizards using the button
        """
        return {
                "name":"Save Precautions",
                "type": "ir.actions.act_window",
                "res_model": "openinvoice.wizard",
                "views": [[False, "form"]],
                "target": "new",
        }