from odoo import http
from odoo.http import request
import json 

class ApiController(http.Controller):
    """
    Description : Creating the rest api for the fetching the patient info 
    """
    @http.route('/api/patients/information', type='http', auth="user", methods=['GET'], csrf=False)
    def get_data(self, **kwargs):
        """
        Description : Creating the rest api to feth the patients data
        """
        # Retrieve data from Odoo model or perform any other logic
        records = request.env['patients.description'].search([])
        data = [{'id': record.id, 'name': record.name} for record in records]
        # Return the data as a JSON response
        return json.dumps(data)
    
    @http.route('/secure', auth='user', methods=['POST','GET'], csrf=True)
    def secure_route(self, **kwargs):
        """
        Description : Creating the api in the post method to save the data  
        """
        request.env['patients.description'].create(kwargs)
        return json.dumps(kwargs)
    
    @http.route('/error_example', auth='public')
    def error_handling(self):
        try:
            # Attempt to fetch data (this could fail)
            data = http.request.env['patients.description'].search([('id', '=', 1)])
            if not data:
                return http.Response("Resource not found", status=404)
            return f"Found record: {data.name}"
        except Exception as e:
            return http.Response(f"Internal Server Error: {str(e)}", status=500)
        
    @http.route('/custom_response', auth='user')
    def custom_response(self):
        response_data = "This is a custom response!"
        headers = {'Content-Type': 'json'}
        return request.make_response(response_data, headers=headers)

