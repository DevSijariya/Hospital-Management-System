from odoo import fields,models
from odoo.exceptions import ValidationError
import re

class InsuranceCompany(models.Model):
    _name="insurance.company"
    name=fields.Char("Name",required=True)
    mobile_number=fields.Char("Mobile_number",required=True)
    email_address=fields.Char("Email Address",required=True)

    def create(self,vals):
        """
        Vaildating the Email and the mobile number before creating the record of the doctor
        """
        existing_email = self.env['doctors.data'].search([('email_address', '=', vals['email_address'])])
        if existing_email:
            raise ValidationError("Email is Already Registered Please Use Another Email")
        match = re.match(r'^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', vals['email_address'])
        if match is None:
            raise ValidationError("Invalid Email Please Use A Valid Email")
        valid_number = re.match(r'^[6-9][0-9]{9}$', str(vals['mobile_number']))
        if valid_number is None:
            raise ValidationError("Invalid Mobile Number Please Enter A Valid Number")
        return super(InsuranceCompany,self).create(vals)

class Insurances(models.Model):
    _name="patient.insurance"
    _rec_name="number"
    number=fields.Char("Number")
    owner=fields.Char("Owner",required=True)
    types=fields.Char('Insurace Type',required=True)
    insuranceCompany=fields.Many2one('insurance.company',string="Insurance Company" , required=True)
    categeory=fields.Char("Categeory")
    start=fields.Datetime("Member Since",required=True)
    end=fields.Datetime("Expiration Date",required=True)


# Genetic Risks

class GeneticRisks(models.Model):
    _name="genetic.risks"
    name=fields.Char("Name",required=True)
    official_name=fields.Char("Official Long Name",required=True)
    affected_chromosomes=fields.Char("Affected Chromosomes",required=True)
    dominance=fields.Char("Dominance")
    location=fields.Char("Location Genes ID Information")
    