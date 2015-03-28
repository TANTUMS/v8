# -*- coding: utf-8 -*-

from openerp import models, fields, api
from datetime import datetime
from dateutil.relativedelta import relativedelta

class mh_campos_extra(models.Model):
	_inherit = 'product.template'

	code   = fields.Integer(string='Code')
	dim_price_vigency_ini = fields.Date('Dim Price Vigency Initial', default=lambda *a:datetime.now().strftime('%Y-%m-%d'))
	dim_price_vigency_fin = fields.Date('Dim Price Vigency Final', default=lambda *a: (datetime.today() + relativedelta(days=1825)).strftime('%Y-%m-%d'))
	employee_price_vigency_ini = fields.Date('Employee Price Vigency Initial',default=lambda *a:datetime.now().strftime('%Y-%m-%d'))
	employee_price_vigency_fin = fields.Date('Employee Price Vigency Final',default=lambda *a: (datetime.today() + relativedelta(days=1825)).strftime('%Y-%m-%d'))
	barcode = fields.Char('BarCode')
	employee_price = fields.Float('Employee Price')
	promotion = fields.Boolean('Promotion',default=False)
	points    = fields.Float('Points')
	product_forecast_01  = fields.Float('Product Forecast 01')
	product_forecast_02  = fields.Float('Product Forecast 02')
	product_forecast_03  = fields.Float('Product Forecast 03')
	product_forecast_04  = fields.Float('Product Forecast 04')
	product_forecast_05  = fields.Float('Product Forecast 05')
	product_forecast_06  = fields.Float('Product Forecast 06')
	product_forecast_07  = fields.Float('Product Forecast 07')
	product_forecast_08  = fields.Float('Product Forecast 08')
	product_forecast_09  = fields.Float('Product Forecast 09')
	product_forecast_10  = fields.Float('Product Forecast 10')
	product_forecast_11  = fields.Float('Product Forecast 11')
	product_forecast_12  = fields.Float('Product Forecast 12')
	mule_sync = fields.Boolean(compute='_actualiza_cambio',default=False,index=True,store=True,string='Mule Sync Flag')

	@api.depends('active','list_price','name','employee_price','barcode','code','promotion','points','employee_price_vigency_ini','employee_price_vigency_fin','dim_price_vigency_ini','dim_price_vigency_fin')
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


class mh_res_partner(models.Model):
	_inherit = 'res.partner'
   
	id_dim       = fields.Integer('ID Dim',readonly=True)
	id_type      = fields.Selection(selection=[(75,'DIM'),(76,'Empleado')], string='Id Type MegaWeb', readonly=True)
	id_sponsor   = fields.Integer('Sponsor')
	calification = fields.Char('Calification', size=1)
	last_name    = fields.Char('Last Name', size=20)
	mother_maiden_name  = fields.Char('MotherMaidenName', size=20)
	is_OfficialId       = fields.Boolean('Id Official ?')
	has_address_proof   = fields.Boolean('Has Adress Proof')
	co_holder           = fields.Char('CoHolder', size=50)
	spouse_name         = fields.Char('Spouse Name', size=50)
	spouse_last_name    = fields.Char('Spouse LastName', size=20)
	spouse_mother_maiden_name  = fields.Char('Spouse Mother Maiden Name', size=20)
	curp                       = fields.Char('CURP', size=25)
	tax_register               = fields.Char('Tax Register', size=50)
	low_date                   = fields.Datetime('Low Date')
	id_bank                    = fields.Integer('ID Bank')
	bank_account               = fields.Char('Bank Account', size=50)
	key_account                = fields.Char('Key bank_account', size=50)
	sucursal                   = fields.Char('Sucursal', size=50)
	id_sex                     = fields.Integer('ID Sex')
	id_marital_status          = fields.Integer('ID Marital Status')
	tax_retention              = fields.Integer('Tax Retention')
	id_iva_group               = fields.Integer('ID Iva Group')
	discount_percent           = fields.Float('Discount Percent')
	exterior_number            = fields.Char('Exterior Number', size=20)
	interior_number            = fields.Char('Interior Number', size=50)
	phone_office               = fields.Char('Phone Office', size=50)
	notes                      = fields.Text('Exterior Number')
	sales_retention            = fields.Integer('Sales Retention')
	point_amount               = fields.Float('Point Amount')
	point_amount_date          = fields.Datetime('Point Amount Date')
	point_amount_in_last_cut   = fields.Float('Point Amount in last Cut')
	credit_amount              = fields.Float('Credit Amount')
	credit_amount_date         = fields.Datetime('Credit Amount Date')
	credit_amountin_last_cut   = fields.Float('Credit Amount in Last Cut')
	consignable                = fields.Boolean('Consignable')
	max_consignable_amount     = fields.Float('Max Consignable Amount')
	consignable_amount         = fields.Float('Consignable Amount')
	consignable_amount_date    = fields.Datetime('Consignable Amount Date')
	consignable_amount_in_last_cut = fields.Float('Consignable Amount in Last Cut')
	need_invoice                   = fields.Boolean('Need Invoice')
	id_difussion_media             = fields.Integer('ID Diffussion Media')
	modified_by                    = fields.Char('Modified By', size=255)
	modified_on                    = fields.Char('Modified On', size=255)
	string1                        = fields.Char('String1', size=50)
	string2                        = fields.Char('String 2', size=50)


#campos extra ventas

class mh_sale_order(models.Model):
	_inherit = 'sale.order'
	
	official_consecutive =  fields.Integer('Official Consecutive')
	id_shop              =  fields.Char('Id Shop', size=12)
	id_dim               =  fields.Integer('Id Dim')
	ref_nova_invoice     =  fields.Char('Nova Invoice' , size=50)
	id_type_dim          =  fields.Integer('Id type Dim')
	id_type_invoice      =  fields.Integer('Id Type Invoice')

#campos extra detalle de ventas

class mh_sale_order_line(models.Model):
	_inherit = 'sale.order.line'

	id_operation_detail  = fields.Char('Operation Detail', size=36)

# campos extra para detalles de invoice

class mh_account_invoice_detail(models.Model):
	_inherit = 'account.invoice.line'

	id_invoice_detail    = fields.Char('Invoice Detail',size=36)

class res_users(models.Model):
    _inherit ='res.users'

    warehouse_uid_id = fields.One2many(comodel_name='stock.warehouse',inverse_name='id', string='Almacen')	