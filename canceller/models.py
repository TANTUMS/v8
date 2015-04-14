# -*- coding: utf-8 -*-

from openerp import models, fields, api,osv

# class canceller(models.Model):
#     _name = 'canceller.canceller'

#     name = fields.Char()

class sale_order(models.Model):
	_inherit = 'sale.order'

	# def do_partial(self,cr,uid,ids,context=None):
	# 	super(stock_partial_picking, self).do_partial(cr,uid,ids,context=context)
	# 	try:

 	def action_auto_cancel(self, cr, uid, ids, context=None):
 		print ids
 		return "Hola mundo"


#      if context is None:
   #          context = {}
   #      sale_order_line_obj = self.pool.get('sale.order.line')
   #      account_invoice_obj = self.pool.get('account.invoice')
   #      procurement_obj = self.pool.get('procurement.order')
   #      for sale in self.browse(cr, uid, ids, context=context):
   #          for inv in sale.invoice_ids:
   #              if inv.state not in ('draft', 'cancel'):
   #                  raise osv.except_osv(
   #                      _('Cannot cancel this sales order!'),
   #                      _('First cancel all invoices attached to this sales order.'))
   #              inv.signal_workflow('invoice_cancel')
   #          procurement_obj.cancel(cr, uid, sum([l.procurement_ids.ids for l in sale.order_line],[]))
   #          sale_order_line_obj.write(cr, uid, [l.id for l in  sale.order_line],
   #                  {'state': 'cancel'})
   #      self.write(cr, uid, ids, {'state': 'cancel'})