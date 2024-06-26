{
    "name":"Real Estate Ads",
    "description":""""
        Sample Module to show available property
    """,
    "version":"1.0",
    "website":"https://www.odoo16.com",
    "author":"Aniket",
    "category":"Sales",
    "depends":['base'],
    "data":[
        'security/ir.model.access.csv',
        'views/property_view.xml',
        'views/property_type_view.xml',
        'views/property_tag_view.xml',
        'views/menu_items.xml',
        
        # Data Files
        #'data/property_type.xml'
        'data/estate.property.type.csv'

    ],

    'demo':[
        'demo/property_tag.xml'
    ],

    "installable":True,
    "application":True,
    "license":"LGPL-3"
}