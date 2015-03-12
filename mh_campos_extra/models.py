# -*- coding: utf-8 -*-

from openerp import models, fields, api

class mh_campos_extra(models.Model):
	_inherit = 'product.product'


	id_type = fields.Integer(string='Id Type')
	code   = fields.Integer(string='Code')
	id_um   = fields.Integer(string='Id UM')
	barcode = fields.Char('BarCode')
	id_iva_type = fields.Integer('Id IVA Type')
	mule_sync = fields.Boolean(string='Mule Sync Flag',default=False,index=True)


#     _name = 'mh_campos_extra.mh_campos_extra'

#     name = fields.Char()