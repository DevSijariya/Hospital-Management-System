from odoo import http
from odoo.http import request,route


class HospitalManagement(http.Controller):
    """
    Description: routing the webpage for the hospital management control
    """
    @route(route=['/hospital/management/page/'], type='http', auth='public',website="True")
    def patient_details(self,**kwargs):
        """
        Description : Creating the Hospital Webpage
        """
        return  request.render('hospital_management_system.webpage')
