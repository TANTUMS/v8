# -*- coding: utf-8 -*-
{
    'name': "canceller",

    'summary': """
       Module to Cancel Automatic Sales Order from Mule """,

    'description': """
        Mule sends sale order to odoo throw xml-rpc, confirm and generate warehouse in
    """,

    'author': "Tantums",
    'website': "http://www.tantums.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Mule',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}