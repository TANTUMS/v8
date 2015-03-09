    # -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
# Coded by: Said Kuri Nunez (skuri@tantums.com)
##############################################################################
{
    'name' : 'Campos_MH_Centroamerica',
    'version' : '1.0',
    'author' : 'Adtech',
    'summary': 'Campos de las tablas de dims que no contiene TantumsERP',
    'description': """
Campos Faltantes        
=====================================================
Campos que contiene Megaweb necesarios para una correcta sincronizacion
    """,
    'category': 'Mrp',
    'sequence': 4,
    'website' : 'http://www.adtech.com.mx',
    'images' : [],
    'depends' : ['base','sale','delivery'],
    'demo' : [],
    'data' : ['view/sale_order_view.xml','view/res_partner_view.xml','view/res_users_view.xml'],
    #,'view/sale_order_search_view.xml'
    'test' : [],
    'auto_install': False,  
    'application': True,
    'installable': True,
}
