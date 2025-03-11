"""
This file contains the patient data and its medical history
"""
import re
import datetime
from odoo import fields, models,api
from odoo.exceptions import UserError,ValidationError

class PatientDescription(models.Model):
    """
    This Class Contains the fields for the patient and the methods use by the patient model
    """
    _name = "patients.description"
    _description = "Patients Data Contains"

    name=fields.Char("Name",required=True)
    age = fields.Integer("Age")
    mobile_number=fields.Char("Mobile_number")
    address=fields.Char("Address", required=True)
    image=fields.Image()
    disease=fields.Many2one('disease.groups',string="Diseases",required=True)
    description=fields.Text("Description")
    date_of_birth = fields.Date("Date of Birth" ,required=True)
    maritial_status=fields.Selection([('single','Single'),('married','Married')])
    gender=fields.Selection([('male','Male'),('female','Female')],required=True)

    blood_type=fields.Selection([('A','A'),('AB','AB'),('O','O'),('B','B'),('Not Known','Not Known')],required=True)
    rh_value=fields.Selection([('+','+'),('-','-')])
    ethnic_group=fields.Selection([('general','General'),('Asian','Asian'),('African','African'),('African American','African American')])
    insurance_company_name=fields.Many2one('insurance.company',string="Insurace Company")
    family=fields.Char("Family")
    recievable=fields.Float("Recievable")
    primary_doctor=fields.Many2one('doctors.data',required=True)
    deceased=fields.Boolean("Deceased")
    bed_taken=fields.Many2one('beddetails.information',string="Bed Occupied")
    appointment_id=fields.One2many('appointment.data','patient_id')
    surgery=fields.One2many('surgery.data','name')
    genetic_risks=fields.Many2many('genetic.risks')
    medicine_id=fields.One2many('medicines.description','prescription_data')


    @api.constrains('bed_taken')
    def _check_unique_bed(self):
        """ Ensure that no two patients occupy the same bed """
        for record in self:
            if record.bed_taken:
                existing_patient = self.env['patients.description'].search([
                    ('bed_taken', '=', record.bed_taken.id),
                    ('id', '!=', record.id)  # Exclude self to avoid checking on update
                ])
                if existing_patient:
                    raise ValidationError(f"{record.bed_taken.name} is already occupied by another patient.")
    @api.constrains('date_of_birth')
    def _calculate_age(self):
        """
        Calculating the age of the patient using the Date of birth
        """
        for record in self:
            if record.date_of_birth<=datetime.date.today():
                if record.date_of_birth:
                    today = datetime.date.today()
                    if today.strftime("%m%d") >= record.date_of_birth.strftime("%m%d"): #Comparing the current month and date with the date of birth month and date
                        record['age'] = today.year - record.date_of_birth.year
                    else:
                        record['age'] = today.year - record.date_of_birth.year - 1
                        if record['age']<=-1:
                            raise ValidationError("Invalid Date Of Birth") # Raising Validation Error for Provding the future date
                else:
                    record['age'] = 0
            else:
                raise ValidationError("Please Provide Correct Date of birth")

    @api.constrains('name')
    def check_name(self):
        """
        Checking the Name of the Patient is correct or not
        """
        for records in self:
            match=re.findall(r'^[a-zA-Z][a-zA-z ]*',records.name)
            if len(match[0])!=len(records.name):
                raise ValidationError("Invaid Patient Name")

    def trigger_birthday(self):
        """
        Description: Triggering the automated actions at every minutes to update the date and time and open the wizards
        """
        patients=self.env['patients.description'].search([])
        for records in patients:
            records.write({"current_date":datetime.datetime.now()})

    def send_mail(self):
        """
        This function is used to send the mail to the patient
        """
        # Fetch the mail template by its ID
        template = self.env['mail.template'].browse(self.env.ref('hospital_management_system.email_send_patient').id)
        # Ensure the template exists
        if template:
            # Send the email using the template
            template.send_mail(self.id, force_send=True)
        else:
            raise UserError("Mail Template not found. Please check the template.")

        notification = {
        'type': 'ir.actions.client',
        'tag': 'display_notification',
        'params': {
            'title': 'Action Not Compelted',
            'type': 'success',
            'message': 'Email Sends Successfully',
            'sticky': False,
        }
        }
        return notification

    def download_patient_card(self):
        """
        This method is used to download the patient id card
        """
        return self.env.ref("hospital_management_system.action_report_patient_template").report_action(self)
