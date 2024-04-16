{
    'name': 'Bista_test1',
    'author':'Aniket',
    'website': 'www.google.com',
    'summary': 'Odoo 16 Development',
    'depends': ['sale'],

    'data': [
        'security/ir.model.access.csv',
        'views/Product_Style.xml',
        'views/rating.xml',
        'views/menu.xml',  
    ],

    "installable": True,
    "application":True,
    "license":"LGPL-3"
}