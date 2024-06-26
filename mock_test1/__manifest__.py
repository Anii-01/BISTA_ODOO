{
    'name': 'Mock Test1',
    'author':'Aniket',
    'website': 'www.google.com',
    'summary': 'Odoo 16 Development',
    'depends': ['sale','base','mail','website'],

    'data': [
        'security/ir.model.access.csv',
        'security/product_style_security.xml',
        'wizard/salespersons_report.xml',
        'report/invoice_report_inherit.xml',
        'views/product_style.xml',
        'views/sale_order_line_inherit.xml',
        'views/product_template.xml',
        'views/customer_view.xml',
        'views/customer_filter.xml',
        'views/invoice_inherit.xml',
        'views/crm_action_button.xml',
        'views/menu.xml',

    ],

    "installable": True,
    "application":True,
    "license":"LGPL-3"
}
