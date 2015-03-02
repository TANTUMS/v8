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
    
    def _shipping(self,cr,uid,ids,shipping_address_sale,arg,context=None):
      so = self.pool.get('sale.order').browse(cr, uid, ids).partner_id.id
      shipping = self.pool.get('res.partner').browse(cr,uid,so)

      shipping_address = str(shipping.mh_shipping_name) + '/' + str(shipping.mh_shipping_street) + '/' + str(shipping.mh_shipping_numin) + '/' + str(shipping.mh_shipping_ext)+ '/' + str(shipping.mh_shipping_colony)
      shipping_address = shipping_address + '/' + str(shipping.mh_shipping_zip)+ '/' + str(shipping.mh_shipping_city)
      res={}
      for r in ids:
          res[r] = shipping_address
      return res

    def _guide(self,cr,uid,ids,shipping_address_sale,arg,context=None):
      so = self.pool.get('sale.order').browse(cr, uid, ids)

      print so.id
      picking_ids = self.pool.get('stock.picking').search(cr,uid,[('group_id','=',so.id)])
      print picking_ids
      picking = self.pool.get('stock.picking').browse(cr,uid,picking_ids)
      print picking
      res={}
      for r in ids:
          res[r] = str(picking.name)+ '\n' + str(picking.carrier_tracking_ref) 
      return res

    _columns = {
                   'shipping_address_sale': fields.function(_shipping,type='text',string='Shipping Adress'),
                   'official_consecutive':  fields.integer('Official Consecutive'),
                   'id_shop': fields.char('Id Shop', size=12),
                   'id_dim' : fields.integer('Id Dim'),
                   'ref_nova_invoice': fields.char('Nova Invoice' , size=50),
                   'package_guide' : fields.function(_guide,type='text',string='Guide')

                }
    

sale_order()

class sale_order_line(osv.osv):
	_inherit = 'sale.order.line'
	_columns = {
				'id_operation_detail': fields.char('Operation Detail', size=36),
				}
sale_order_line()