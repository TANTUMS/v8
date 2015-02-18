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

from openerp.tools.translate import _
from openerp.osv import osv, fields
import datetime
import openerp.exceptions
import openerp.addons

class res_partner(osv.osv):
    _inherit = 'res.partner'
    _columns = {
                'id_dim'     : fields.integer('ID Dim'),
                'id_type'    : fields.integer('Id Type MegaWeb'),
                'id_sponsor' : fields.integer('Sponsor'),
                'calification': fields.char('Calification', size=1),
                'last_name'   : fields.char('Last Name', size=20),
                'mother_maiden_name'  : fields.char('MotherMaidenName', size=20),
                'is_OfficialId'   : fields.boolean('Id Official ?'),
                'has_address_proof'   : fields.boolean('Has Adress Proof'),
                'co_holder'  : fields.char('CoHolder', size=50),
                'spouse_name'  : fields.char('Spouse Name', size=50),
                'spouse_last_name'  : fields.char('Spouse LastName', size=20),
                'spouse_mother_maiden_name'  : fields.char('Spouse Mother Maiden Name', size=20),
                'curp'  : fields.char('CURP', size=25),
                'tax_register'  : fields.char('Tax Register', size=50),
                'low_date'  : fields.datetime('Low Date'),
                'id_bank'     : fields.integer('ID Bank'),
                'bank_account'  : fields.char('Bank Account', size=50),
                'key_account'  : fields.char('Key bank_account', size=50),
                'sucursal'  : fields.char('Sucursal', size=50),
                'id_sex'     : fields.integer('ID Sex'),
                'id_marital_status'     : fields.integer('ID Marital Status'),
                'tax_retention'     : fields.integer('Tax Retention'),
                'id_iva_group'     : fields.integer('ID Iva Group'),
                'discount_percent' : fields.float('Discount Percent'),
                'exterior_number'  : fields.char('Exterior Number', size=20),
                'interior_number'  : fields.char('Interior Number', size=50),
                'phone_office'  : fields.char('Phone Office', size=50),
                'notes'  : fields.text('Exterior Number'),
                'sales_retention'   : fields.integer('Sales Retention'),
                'point_amount'      : fields.float('Point Amount'),
                'point_amount_date'  : fields.datetime('Point Amount Date'),
                'point_amount_in_last_cut'      : fields.float('Point Amount in last Cut'),
                'credit_amount'      : fields.float('Credit Amount'),
                'credit_amount_date'  : fields.datetime('Credit Amount Date'),
                'credit_amountin_last_cut'      : fields.float('Credit Amount in Last Cut'),
                'consignable'   : fields.boolean('Consignable'),
                'max_consignable_amount' : fields.float('Max Consignable Amount'),
                'consignable_amount' : fields.float('Consignable Amount'),
                'consignable_amount_date': fields.datetime('Consignable Amount Date'),
                'consignable_amount_in_last_cut' : fields.float('Consignable Amount in Last Cut'),
                'need_invoice'   : fields.boolean('Need Invoice'),
                'id_difussion_media': fields.integer('ID Diffussion Media'),
                'modified_by': fields.char('Modified By', size=255),
                'modified_on': fields.char('Modified On', size=255),
                'string1': fields.char('String1', size=50),
                'string2': fields.char('String 2', size=50),
                }
res_partner()