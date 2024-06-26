{
    'name': 'Hospital Management System',
    'author':'Aniket',
    'website': 'www.google.com',
    'summary': 'Odoo 16 Development',
    'depends': ['sale','base','mail'],

    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'security/security2.xml',
        #'data/sequence.xml',
        'data/mail_template.xml',
        'data/sale_order_mail_template.xml',
        'wizard/create_appointment.xml',
        'wizard/product_add_wizard_sale.xml',
        'wizard/product_add_wizard_view.xml',
        'wizard/sale_order_wizard_report_view.xml',

        'views/patient.xml',
        'views/doctor.xml',
        'views/doctor_type.xml',
        'views/Appointments.xml',
        'views/sale_order_xls_report.xml',
        #'views/trail.xml',
        'views/lab.xml',
        'report/reports.xml',
        'report/reports_template.xml',
        #'report/sale_report_inherit.xml',
        'report/optional_product_report.xml',
        'report/optional_product_template.xml',
        'report/report_wizard_template.xml',
        'report/report_wizard.xml',
        'report/doctor_server_action.xml',
        'views/menu.xml',
        
    ],

    "installable": True,
    "application":True,
    "license":"LGPL-3"
}
