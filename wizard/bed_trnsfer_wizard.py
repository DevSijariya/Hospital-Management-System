"""
popup the form view wizard and transfer the bed of the patietn
"""
from odoo import fields, models, api

class BedTransferWizard(models.TransientModel):
    """
    
    """
    _name = "bedtransfer.wizard"
    _description = "Transferring the bed of the patient"

    patient_id = fields.Many2one("patients.description", string="Patient", required=True)
    shift_bed_ = fields.Char("Shift Bed")
    shift_bed_to = fields.Many2one('beddetails.information',string="Shift To")
    reason = fields.Char("Reason")

    @api.model
    def default_get(self, fields_list):
        """ Auto-fill shift_from with current hospital_bed of the patient """
        res = super(BedTransferWizard, self).default_get(fields_list)
        active_id = self.env.context.get('active_id')  # Get active record ID
        if active_id:
            admin_data = self.env['administrative.data'].browse(active_id)
            res['patient_id'] = admin_data.patient_id.id
            res['shift_bed_'] = admin_data.hospital_bed
        return res

    def transfer_bed(self):
        """ Create a new bed record and update patient model """
        self.shift_bed_=self.patient_id.bed_taken.name
        
        if not self.shift_bed_to:
            raise ValueError("Please select a bed to transfer.")

        # 1. Create a new record in bed.info
        self.env['bed.info'].create({
            'patient_id': self.patient_id.id,
            'shiftdate': fields.Datetime.now(),
            'shift_bed_from_': self.shift_bed_,
            'shift_bed_to_': self.shift_bed_to.name,
            'shift_reason': self.reason,
        })

        # 2. Update administrative model (hospital_bed field)
        admin_record = self.env['administrative.data'].search([('patient_id', '=', self.patient_id.id)], limit=1)
        patient_record = self.env['patients.description'].browse(self.patient_id.id)
        if admin_record:
            admin_record.write({'hospital_bed': self.shift_bed_to.name})
            patient_record.write({'bed_taken':self.shift_bed_to.id})

        return {"type": "ir.actions.act_window_close"}
