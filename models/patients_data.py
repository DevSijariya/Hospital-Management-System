from odoo import fields, models,api
from odoo.exceptions import UserError,ValidationError
from odoo.http import request
import datetime
import re

class PatientDescription(models.Model):
    _name = "patients.description"
    _description = "Patients Data Contains"

    name=fields.Char("Name",required=True)
    age = fields.Integer("Age",compute="_compute_age",required=True)
    mobile_number=fields.Char("Mobile_number")
    address=fields.Char("Address")
    image=fields.Image()
    disease=fields.Char("Diseases")
    description=fields.Text("Precautions")
    date_of_birth = fields.Date("Date of Birth" ,required=True)
    maritial_status=fields.Selection([('single','Single'),('married','Married')])
    gender=fields.Selection([('male','Male'),('female','Female')])
    
    blood_type=fields.Selection([('A','A'),('AB','AB'),('O','O'),('B','B')])
    rh_value=fields.Selection([('+','+'),('-','-')])
    ethnic_group=fields.Selection([('general','General'),('Asian','Asian'),('African','African'),('African American','African American')])
    insurance_company_name=fields.Char("Insaurance Company Name")
    family=fields.Char("Family")
    recievable=fields.Float("Recievable")
    primary_doctor=fields.Many2one('res.partner')
    deceased=fields.Boolean("Deceased")
    bed_occupied=fields.Selection([('Bed 1','Bed 1'),('Bed 2','Bed 2'),('Bed 3','Bed 3'),('Bed 4','Bed 4')])

    @api.constrains('bed_occupied')
    def _check_unique_bed(self):
        """ Ensure that no two patients occupy the same bed """
        for record in self:
            if record.bed_occupied:
                existing_patient = self.env['patients.description'].search([
                    ('bed_occupied', '=', record.bed_occupied),
                    ('id', '!=', record.id)  # Exclude self to avoid checking on update
                ])
                if existing_patient:
                    raise ValidationError(f"Bed {record.bed_occupied} is already occupied by another patient.")


    def create(self,vals):
        return super(PatientDescription,self).create(vals)

    def _compute_age(self):
        """
        Calculating the age of the patient using the Date of birth
        """
        for record in self:
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
    
    
    
    @api.constrains('name')
    def _check_name(self):
        """
        Checking the Name of the Patient is correct or not
        """
        for records in self:
            match=re.match(r'^[a-zA-Z][a-zA-z ]*',records.name)
            if match is None:
                raise ValidationError("Invaid Patient Name")
            

    
        
    def trigger_birthday(self):
        """
        Description: Triggering the automated actions at every minutes to update the date and time and open the wizards
        """
        # import pdb;pdb.set_trace()
        patients=self.env['patients.description'].search([])
        for records in patients:
            records.write({"current_date":datetime.datetime.now()})  
        
        
            

    def send_mail(self):
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
    

    def download_Patient_Card(self):
        return self.env.ref("hospital_management_system.action_report_patient_template").report_action(self)
    
