{
    'name': "Hospital_Management",
    'version': '18.0',
    'depends': ['base','mail','website'],
    'author': "Codetrade",
    'category': 'Management',
    'description': """
        This is the custom Hospital Management model contain Data About the Doctors and the Patients 
    """,
    # data files always loaded at installation
    # xml file and security file are imported in data
    'data': [
        'security/hospital_data_access.xml',
        'security/ir.model.access.csv',

        
        'wizard/birthday_popup.xml',
        'wizard/patient_wizard.xml',
        'wizard/open_invoice_wizard.xml',
        'wizard/bed_transfer_wizard.xml',

        'data/ir_cron.xml',
        'data/ir_sequence.xml',

        'report/paper_format.xml',
        'report/ir_action_report.xml',
        'report/patient_card.xml',
        'report/patient_appointment_template.xml',
        'report/patient_prescription.xml',

        'views/patient_view.xml',
        'views/prescription_data.xml',
        'views/appointment_view.xml',
        'views/medicines_view.xml',
        'views/administrative_data.xml',
        'views/bed_info_detail.xml',
        'views/patient_icu.xml',
        'views/mechanical_ventilator.xml',
        'views/doctor_view.xml',
        'views/new_button.xml',
        'views/hospital_webpage.xml',
        'views/mail_template_patient.xml',
        'views/patient_server_actions.xml',
        'views/webpage_module.xml',
        'views/webpage_doctor.xml',
        'views/webpage_display_patients_info.xml',
    ],
    'assets': {
        'web.assets_backend': [
        'hospital_management_system/static/src/js/button.js',
        'hospital_management_system/static/src/js/form_button.js',
        'hospital_management_system/static/src/js/kanban_button.js',
    
        'hospital_management_system/static/src/xml/button.xml',
        'hospital_management_system/static/src/xml/form_button.xml',
        'hospital_management_system/static/src/xml/kanban_button.xml',

 
        ],
        },


    # data files containing optionally loaded demonstration data
    'demo': [
        # 'demo/demo_data.xml',
    ],
    'license':'LGPL-3',
    'installable':True,
    'application':True,
}
