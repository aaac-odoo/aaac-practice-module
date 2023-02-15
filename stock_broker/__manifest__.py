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
        'views/stock_price_view.xml',
        'views/category_view.xml',
        'views/portfolio_view.xml',
        'views/consultant_view.xml',
        'views/sip_cron_job_records.xml',
        'views/sip_view.xml',
        'views/menus.xml',
    ],

    'demo':[
        'demo/demo_data.xml'
    ],
    'installable': True,
    'application': True,
}    