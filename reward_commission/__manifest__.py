# -*- coding: utf-8 -*-

{
    'name' : 'Reward Commission',
    'version' : '1.5',
    'summary': 'Reward to resellers and hairdressers by commisions',
    'category': 'Tools',
    'depends' : [
        'survey',
        'crm',
        'sale',
        'purchase',
        'website_sale',
        'l10n_es',
        'survey',
        'base_geolocalize',
        'website',

    ],
    'data': [
    'data/product.xml',
    'data/geo_localize_partner.xml',

    #backend
    'views/backend/res_partner_form.xml',
    'views/backend/survey_view_input.xml',
    'views/backend/res_config.xml',
    'views/backend/sale_order_form_view.xml',

    #frontend
    'views/frontend/assets.xml',
    'views/frontend/payment.xml',
    'views/frontend/portal.xml',
    ],



    'qweb': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,

}
