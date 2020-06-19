# -*- coding: utf-8 -*-

{
    'name' : 'Reward Commission',
    'version' : '1.1',
    'summary': 'Reward to resellers and hairdressers by commisions',
    'category': 'Tools',
    'depends' : ['survey','crm','sale','purchase','website_sale','l10n_es','survey',],
    'data': [
    'data/product.xml',

    'views/backend/res_partner_form.xml',
    'views/backend/survey_view_input.xml',
    'views/backend/res_config.xml',
    'views/backend/sale_order_form_view.xml',],

    'qweb': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,

}
