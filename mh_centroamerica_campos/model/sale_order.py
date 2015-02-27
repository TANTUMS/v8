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


class sale_order(osv.osv):
    _inherit = 'sale.order'
    _columns = {
                   'shipping_address_sale': fields.text('Śhipphing Address'),
                   'official_consecutive':  fields.integer('Official Consecutive'),
                   'id_shop': fields.char('Id Shop', size=12),
                   'id_dim' : fields.integer('Id Dim'),
                   'ref_nova_invoice': fields.char('Nova Invoice' , size=50),
                }
sale_order()