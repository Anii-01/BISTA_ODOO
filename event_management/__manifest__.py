{
    'name':'Event Management',
    'website':'www.em.com',
    'author':'Siddharth Sharma',
    'version': '1.0',
    'category': 'Uncategorized',
    'summary': 'Manage events, attendees, organizers, and registrations.',
    'depends': ['base','mail','portal','website'],
    'data':[
        #Security Files
        'security/ir.model.access.csv',
        #'security/access_rule.xml',
        #'security/groups.xml',
        'security/portal_groups.xml',

        #wizard
        'wizard/registration_xls_document.xml',

        #report
        'report/event_report_template.xml',
        'report/event_report_action.xml',

        #Views Files
        'views/event_event_view.xml',
        'views/event_attendee_view.xml',
        'views/event_organizer_view.xml',
        'views/event_registration_view.xml',
        'views/menu_view.xml',
        #'views/template.xml',
        'views/portal_template.xml',

        #Data Files
        'data/email_template.xml',
        'data/registration_website_menu.xml',
        'data/attendee_website_menu.xml',

        #website
        'website/web_menu.xml',
    ],
    'application': True,
    'installable': True,
    'license':'LGPL-3',

}
