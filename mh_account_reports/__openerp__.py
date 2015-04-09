# -*- coding: utf-8 -*-
{
    'name': "mh_account_reports",

    'summary': """
        Accounting Reports for MH Guatemala""",

    'description': """
        Reportes para proyecto de Mh guatemala entre ellos

            - Reporte de cuadre de Montos en Ventas contra Facturacion contra Cobros
    """,

    'author': "Adtech",
    'website': "http://www.adtech.com.mx",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'MH',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','account'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'templates.xml' ,'view/account_report.xml','view/report_incomes_match.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}