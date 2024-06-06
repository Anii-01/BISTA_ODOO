{
    'name': 'Event Management',
    'author':'Aniket',
    'website': 'www.google.com',
    'summary': 'Odoo 16 Development',
    'depends': ['base'],

    'data': [
        'security/ir.model.access.csv',
        'security/event_management_security.xml',
        #'wizard/registartion_details_wizard.xml',
        'views/event_attendee_view.xml',
        'views/event_view.xml',
        'views/event_registration_view.xml',
        'views/event_organizer_view.xml',
        'views/menu.xml',
        
    ],

    "installable": True,
    "application":True,
    "license":"LGPL-3"
}
