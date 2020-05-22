# -*- coding: utf-8 -*-
{
    'name': "portal_users_customization",

    'summary': """
        Limit specific product categories to portal users
        """,

    'description': """
        Limit specific product categories to portal users
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base',
                'website_sale',
                'website_event_sale'],

    # always loaded
    'data': [
        'security/security.xml',
        'views/views.xml',
    ],
}
