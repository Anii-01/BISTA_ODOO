{
    'name': 'Bista Project1',
    'author':'Aniket',
    'website': 'www.google.com',
    'summary': 'Odoo 16 Development',
    'depends': ['sale','base','mail'],

    'data': [
        'security/ir.model.access.csv',
        #'security/security1.xml',
        #'wizard/TestWizard.xml',
        #'views/bista_employee.xml',
        #'views/bista_order_line_view.xml',
        #'views/sale_order_inherit2.xml',
        #'report/sale_order_report_inherit.xml',
        #'views/delivery_days.xml',
        #'data/day_of_week_data.xml',
        'views/menu.xml',
        
    ],

    "installable": True,
    "application":True,
    "license":"LGPL-3"
}



