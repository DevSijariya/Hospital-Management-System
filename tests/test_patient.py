from odoo.tests import TransactionCase
import logging

_logger = logging.getLogger(__name__)


_logger.warning('Before Class')

class TestModulePatient(TransactionCase):
    """
    Description : Creating the testing class which can test the patient model functionality
    """
    def setUpClass(cls):
       super(TestModulePatient, cls).setUpClass()

    _logger.warning('Inside Class')

    def check_patient_age(self):
        patient=self.env['patients.description'].create({
            'name':'test_1',
            'mobile_number':'8888888888',
            'date_of_birth':"2000-01-01"
        })
        self.assertEqual(patient.name, 'test_1')
        self.assertEqual(patient.mobile_number,'8888888888')
        self.assertEqual(patient.age, 25)
        
  