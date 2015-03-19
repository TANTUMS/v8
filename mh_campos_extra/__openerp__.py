# -*- coding: utf-8 -*-
{
    'name': "mh_campos_extra",

    'summary': """
        Campos extra para proyecto MH Centroamerica
        """,

    'description': """
        Campos extra para proyecto MH Centroamerica
            - Productos
    """,

    'author': "Adtech",
    'website': "http://www.adtech.com.mx",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'MH',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale','mrp'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'templates.xml','view/product_product_view.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}