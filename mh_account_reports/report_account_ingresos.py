from openerp.osv import osv,orm
from openerp import models, fields, api
from openerp.report import report_sxw
import pytz
import datetime, time
from openerp import SUPERUSER_ID
import pdb

class wizard_mh_account(models.TransientModel):
    _name = 'wizard.mh.account'
    
    date_report = fields.Date('Fecha', default=lambda *a: datetime.date.today().strftime('%Y-%m-%d'))
        # 'birth_edate': fields.date('End Date'),
    def print_report(self,cr,uid,ids,context=None):
        datas = {}
        datas = {'ids': context.get('active_ids', [])}
        datas['model'] = 'wizard.mh.account'
        datas['form'] = self.read(cr, uid, ids)[0]
        return {
            'type': 'ir.actions.report.xml',
            'report_name': 'mh_account_reports.report_incomes_match_template',
            'datas':datas,      
            'report_type' : 'pdf',
        }

class payslip_report(report_sxw.rml_parse):

    def __init__(self, cr, uid, name, context):
        super(payslip_report, self).__init__(cr, uid, name, context)
        self.localcontext.update({
            'get_sales':self.get_sales,
            'get_invoices': self.get_invoices,
            'get_vouchers' : self.get_vouchers,
            'get_id_shops' : self.get_id_shops,
            'get_company' : self.get_company,
        })


    def get_id_shops(self):

        idshops= self.pool.get('account.cost.center')
        idshops_id=idshops.search(self.cr,self.uid,[]) # All cost center
        shop_obj=idshops.browse(self.cr,self.uid,idshops_id)
        return shop_obj

    def get_company(self):
        company = self.pool.get('res.company')  
        return company.browse(self.cr,self.uid,1)


    def get_invoices(self,fecha,shop):
        # get user's timezone
        user_pool = self.pool.get('res.users')
        user = user_pool.browse(self.cr, SUPERUSER_ID, self.uid)
        tz = pytz.timezone(user.partner_id.tz) or pytz.utc
        # get localized dates
        fecha_final = pytz.utc.localize(datetime.datetime.strptime(fecha + ' 23:59:59', '%Y-%m-%d %H:%M:%S')).astimezone(tz)
        fecha = pytz.utc.localize(datetime.datetime.strptime(fecha + ' 00:00:00', '%Y-%m-%d %H:%M:%S')).astimezone(tz)
        # date_to   = pytz.utc.localize(datetime.datetime.strptime(date_to, DATETIME_FORMAT)).astimezone(tz)
        invoices = self.pool.get('account.invoice')
        invoices_ids = invoices.search(self.cr,self.uid,[('date_invoice' ,'>=' ,fecha),('date_invoice' ,'<=' ,fecha_final),('cost_center_id','=',shop)])
        res = []
        ids = []
        if fecha:
            res = invoices.browse(self.cr, self.uid, invoices_ids)
        return res

    def get_sales(self,fecha,shop):

        # get user's timezone
        user_pool = self.pool.get('res.users')
        user = user_pool.browse(self.cr, SUPERUSER_ID, self.uid)
        tz = pytz.timezone(user.partner_id.tz) or pytz.utc

        # get localized dates
        if fecha:
            fecha_final =  pytz.utc.localize(datetime.datetime.strptime(fecha + ' 23:59:59', '%Y-%m-%d %H:%M:%S')).astimezone(tz)
            fecha = pytz.utc.localize(datetime.datetime.strptime(fecha + ' 00:00:00', '%Y-%m-%d %H:%M:%S')).astimezone(tz)
            
        # date_to   = pytz.utc.localize(datetime.datetime.strptime(date_to, DATETIME_FORMAT)).astimezone(tz)
        fecha=str(fecha)
        fecha_final=str(fecha_final)
        sales = self.pool.get('sale.order')
        sales_ids = sales.search(self.cr,self.uid,[('date_order' ,'>=' ,fecha),('date_order' ,'>=' ,fecha_final),('centro_costo_id','=',shop)])
        res = []
        ids = []
        if fecha:
            res = sales.browse(self.cr, self.uid, sales_ids)
        return res


    def get_vouchers(self,fecha,shop):
        # get user's timezone
        user_pool = self.pool.get('res.users')
        user = user_pool.browse(self.cr, SUPERUSER_ID, self.uid)
        tz = pytz.timezone(user.partner_id.tz) or pytz.utc
        # get localized dates
        fecha_final = pytz.utc.localize(datetime.datetime.strptime(fecha + ' 23:59:59', '%Y-%m-%d %H:%M:%S')).astimezone(tz)
        fecha = pytz.utc.localize(datetime.datetime.strptime(fecha + ' 00:00:00', '%Y-%m-%d %H:%M:%S')).astimezone(tz)
        # date_to   = pytz.utc.localize(datetime.datetime.strptime(date_to, DATETIME_FORMAT)).astimezone(tz)
        vouchers = self.pool.get('account.voucher')
        vouchers_ids = vouchers.search(self.cr,self.uid,[('date' ,'>=' ,fecha),('date' ,'<=' ,fecha_final),('id_shop','=',shop)])
        res = []
        ids = []
        if fecha:
            res = vouchers.browse(self.cr, self.uid, vouchers_ids)
        return res

class wrapped_report_payslip(orm.AbstractModel):
    _name = 'report.mh_account_reports.report_incomes_match_template'
    _inherit = 'report.abstract_report'
    _template = 'mh_account_reports.report_incomes_match_template'
    _wrapped_report_class = payslip_report

    def render_html(self, cr, uid, ids, data=None, context=None):
        if context is None:
            context = {}
        #either remove active_ids, active_model from context
        if context and context.get('active_ids'):
            context.pop('active_ids')
            context.pop('active_model')
        #or update the context by taking values from data dictionary which was passed from wizard (sample code)
        if data:
            context.update({'active_model': 'account.invoice', 'active_ids': 1, 'form':data.get('form', {}).get(str('date_report'), [])})
        return super(wrapped_report_payslip, self).render_html(cr, uid, ids, data=data, context=context)
