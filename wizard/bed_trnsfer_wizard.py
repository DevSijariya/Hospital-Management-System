from odoo import fields, models, api

class BedTransferWizard(models.TransientModel):
    _name = "bedtransfer.wizard"
    _description = "Transferring the bed of the patient"

    patient_id = fields.Many2one("patients.description", string="Patient", required=True)
    shift_from = fields.Selection([('Bed 1', 'Bed 1'), ('Bed 2', 'Bed 2'), ('Bed 3', 'Bed 3'), ('Bed 4', 'Bed 4')],
                                  string="Shift From", readonly=True)
    shift_to = fields.Selection([('Bed 1', 'Bed 1'), ('Bed 2', 'Bed 2'), ('Bed 3', 'Bed 3'), ('Bed 4', 'Bed 4')],
                                string="Shift To", required=True)
    reason = fields.Char("Reason")

    @api.model
    def default_get(self, fields_list):
        """ Auto-fill shift_from with current hospital_bed of the patient """
        res = super(BedTransferWizard, self).default_get(fields_list)
        active_id = self.env.context.get('active_id')  # Get active record ID
        if active_id:
            admin_data = self.env['administrative.data'].browse(active_id)
            res['patient_id'] = admin_data.patient_id.id
            res['shift_from'] = admin_data.hospital_bed
        return res

    def transfer_bed(self):
        """ Create a new bed record and update patient model """
        if not self.shift_to:
            raise ValueError("Please select a bed to transfer.")

        # 1. Create a new record in bed.info
        new_bed_record = self.env['bed.info'].create({
            'patient_id': self.patient_id.id,
            'shiftdate': fields.Datetime.now(),
            'shift_from': self.shift_from,
            'shift_to': self.shift_to,
            'shift_reason': self.reason,
        })

        # 2. Update administrative model (hospital_bed field)
        admin_record = self.env['administrative.data'].search([('patient_id', '=', self.patient_id.id)], limit=1)
        if admin_record:
            admin_record.write({'hospital_bed': self.shift_to})

        return {"type": "ir.actions.act_window_close"}  # Close wizard
