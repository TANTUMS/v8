# -*- coding: utf-8 -*-

from openerp import models, fields, api

class mh_campos_extra(models.Model):
	_inherit = 'product.template'

	code   = fields.Integer(string='Code')
	barcode = fields.Char('BarCode')
	employee_price = fields.Float('Employee Price')
	promotion = fields.Boolean('Promotion',default=False)
	mule_sync = fields.Boolean(compute='_actualiza_cambio',default=False,index=True,store=True,string='Mule Sync Flag')

	@api.depends('active','list_price','name','employee_price','barcode','code','promotion')
	def _actualiza_cambio(self):
		for rec in self:
			self.mule_sync = False

class mh_campos_extra_mrp(models.Model):
	_inherit = 'mrp.bom.line'

	bom_mule_sync = fields.Boolean(compute='_actualiza_cambio_mrp',default=False,index=True,store=True,string='Mule Sync Flag')

	@api.depends('product_id','product_qty','product_uom')
	def _actualiza_cambio_mrp(self):
		for rec in self:
			self.bom_mule_sync = False