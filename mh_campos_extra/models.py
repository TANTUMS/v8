# -*- coding: utf-8 -*-

from openerp import models, fields, api

class mh_campos_extra(models.Model):
	_inherit = 'product.template'

	code   = fields.Integer(string='Code')
	barcode = fields.Char('BarCode')
	employee_price = fields.Float('Employee Price')
	mule_sync = fields.Boolean(compute='_actualiza_cambio',default=False,index=True,store=True,string='Mule Sync Flag')

	@api.depends('active','list_price','name','employee_price','barcode','code')
	def _actualiza_cambio(self):
		for rec in self:
			self.mule_sync = False