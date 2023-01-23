# -- coding: utf-8 --

{
'name': 'Stock Broker',
    'version': '1',
    'sequence': 1,
    'summary': 'Buy and Sell stocks.',
    'description': "--demo description--",

    'data': [
        'security/ir.model.access.csv',
        'views/order_view.xml',
        'views/listed_company_views.xml',
        'views/user_view.xml',
        'views/menus.xml',
    ],
    'installable': True,
    'application': True,
}    