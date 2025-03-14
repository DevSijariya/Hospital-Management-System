"""
Doctor Class 
"""
import re
from odoo import fields, models
from odoo.exceptions import ValidationError

class DoctorData(models.Model):
    """
    Used to contain the doctors information
    """
    _name = "doctors.data"
    _description = "Patients Data Contains"

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
        return super(DoctorData,self).create(vals)


class PhysicainProffesionalInfo(models.Model):
    _name="physician.proffesional.info"
    name=fields.Many2one("doctors.data",string="Name",required=True)
    physician_id=fields.Char("Id")
    institution=fields.Many2one('healthcenter.building',string="Institution",required=True)
    speciality=fields.Char("Speciality",required=True)
