from odoo import http
from odoo.http import request,route


class HospitalManagementPage(http.Controller):
    """
    Description: routing the webpage for the hospital management control
    """
    @route(route=['/'], type='http', auth='public',website="True")
    def hospital_management(self,**kwargs):
        """
        Description : Creating the Hospital Webpage
        """
        return  request.render('hospital_management_system.homepage_id')

    @route(route=['/patient/information'],type='http',auth='public',website="True")
    def patient_info(self):
        patient_details = request.env['patients.description'].sudo().search([])
        return request.render('hospital_management_system.patient_info',{'my_details':patient_details})
    
    @route('/patient/information/id/<model("patients.description"):patient>', type='http', auth='public', website=True)
    def web_form_submit(self, **post):
        patient_details = request.env['patients.description'].sudo().browse(post['patient']['id'])
        return request.render('hospital_management_system.patient_information_display',{'patient':patient_details})
    
class DoctorView(http.Controller):
    @route(route=['/doctor/information'], type='http', auth='public',website="True")
    def patient_details(self,**kwargs):
        """
        Description : Getting the patient details from the model 
        """
        doctor_details = request.env['doctors.data'].sudo().search([])
        return  request.render('hospital_management_system.doctor_data_display', {'my_details': doctor_details})
    

    @route('/doctor/information/<model("doctors.data"):doctor>', type='http', auth='public', website=True)
    def web_form_submit(self, **post):
        doctor_details = request.env['doctors.data'].sudo().browse(post['doctor']['id'])
        return request.render('hospital_management_system.doctor_information_view',{'patient':doctor_details})


class DoctorsDataAdd(http.Controller):
    @route('/doctor/information/create', type='http', auth='public',website=True)
    def patient_details(self):
        return  request.render('hospital_management_system.doctor_form_view')
    
    @route('/doctor/information/submit', type='http', auth='public', website=False)
    def web_form_submit(self, **post):
        request.env['doctors.data'].sudo().create({
                    'name': post.get('name'),
                    'mobile_number': post.get('mobile_number'),
                    'email_address': post.get('email_address'),
                    'address': post.get('address'),
                })
        return request.redirect('/doctor/information')
    @route('/doctor/unlink/<model("doctors.data"):doctor>' ,type='http', auth='public', website=True)
    def del_dr_info(self,**post):
        """
        Description : Used to delete the data
        """
        request.env['doctors.data'].browse(post['doctor']['id']).unlink()
        return request.redirect('/doctor/information')
        
    
    
class PatientCreate(http.Controller):
    @route('/patient/add/information/form', type='http', auth='public',website=True)
    def patient_details(self):
        """
        Description : Return the webpage to display the patient details
        """
        medicines=request.env['medicines.description'].search([])
        return  request.render('hospital_management_system.patient_add_data_template',{'medicines':medicines})
    
    @route('/patient/data/submit/form', type='http', auth='public', website=False)
    def web_form_submit(self, **post):
        """
        Description : Creating the new record using the webpage/ Update the information
        """
        med_ids = request.httprequest.args.getlist('medicine[]')
        medicines = request.env['medicines.description'].browse([int(med_id) for med_id in med_ids])
 
        patient_present=request.env['patients.description'].search([('email_address','=',post.get('email_address'))])
        if patient_present:
            request.env['patients.description'].browse(patient_present.id).write({
                'name': post.get('name'),
                'mobile_number': post.get('mobile_number'),
                'email_address': post.get('email_address'),
                'address': post.get('address'),
                'disease': post.get('disease'),
                'date_of_birth': post.get('date_of_birth'),
                'medicines_id': [(6, 0, medicines.ids)]
        
            })
        else:
            request.env['patients.description'].sudo().create({
                        'name': post.get('name'),
                        'mobile_number': post.get('mobile_number'),
                        'email_address': post.get('email_address'),
                        'address': post.get('address'),
                        'disease':post.get('disease'),
                        'date_of_birth': post.get('date_of_birth'),
                        'medicines_id': [(6, 0, medicines.ids)]

                        
                    })
        return request.redirect('/patient/information')
    @route('/info/unlink/<model("patients.description"):patient>' ,type='http', auth='public', website=True)
    def del_info(self,**post):
        """
        Description : Used to delete the data
        """
        request.env['patients.description'].browse(post['patient']['id']).unlink()
        return request.redirect('/patient/information')
        