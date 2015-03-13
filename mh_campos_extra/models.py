# -*- coding: utf-8 -*-

from openerp import models, fields, api

# class mh_campos_extra(models.Model):
# 	_inherit = 'product.product'

# 	id_type = fields.Integer(string='Id Type')
# 	code   = fields.Integer(string='Code')
# 	id_um   = fields.Integer(string='Id UM')
# 	barcode = fields.Char('BarCode')
# 	id_iva_type = fields.Integer('Id IVA Type')
# 	#mule_sync = fields.Boolean(string='Mule Sync Flag',default=False,index=True)
# 	mule_sync = fields.Boolean(compute='_actualiza_cambio',default=False,index=True,store=True,string='Mule Sync Flag')

# 	@api.depends('default_code','active','product_tmpl_id.list_price','product_tmpl_id.name')
# 	def _actualiza_cambio(self):
# 		for rec in self:
# 			self.mule_sync = False


class mh_campos_extra(models.Model):
	_inherit = 'product.template'

	code   = fields.Integer(string='Code')
	barcode = fields.Char('BarCode')
	mule_sync = fields.Boolean(compute='_actualiza_cambio',default=False,index=True,store=True,string='Mule Sync Flag')

	@api.depends('active','list_price','name')
	def _actualiza_cambio(self):
		for rec in self:
			self.mule_sync = False