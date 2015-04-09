# from openerp import api, models

# class ParticularReport(models.AbstractModel):
#     _name = 'report.mh_account_reports.report_without_prices'
    
    

#     @api.multi
#     def render_html(self, data=None):
#         report_obj = self.env['report']
#         self.env['report']
#         print self.env['ids']
#         print ids
#         report = report_obj._get_report_from_name('mh_account_reports.report_without_prices')
#         docargs = {
#             'doc_ids': ids,
#             'doc_model': report.model,
#             'docs': self.env[report.model].browse(ids),
            
#         }   
#         print docargs
#         return report_obj.render('mh_account_reports.report_without_prices', docargs)
from openerp.osv import osv
from openerp.report import report_sxw
import pytz
import datetime, time
from openerp import SUPERUSER_ID


class payslip_report(report_sxw.rml_parse):

    def __init__(self, cr, uid, name, context):
        super(payslip_report, self).__init__(cr, uid, name, context)
        self.localcontext.update({
            'get_sales':self.get_sales,
            'get_invoices': self.get_invoices,
            'get_vouchers' : self.get_vouchers
        })






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
        print invoices
        invoices_ids = invoices.search(self.cr,self.uid,[('date_invoice' ,'>=' ,fecha),('date_invoice' ,'<=' ,fecha_final),('cost_center_id','=',shop)])
        print invoices_ids
        res = []
        ids = []
        if fecha:
            res = invoices.browse(self.cr, self.uid, invoices_ids)
            print res
        return res

    def get_sales(self,fecha):


        # get user's timezone
        user_pool = self.pool.get('res.users')
        user = user_pool.browse(self.cr, SUPERUSER_ID, self.uid)
        tz = pytz.timezone(user.partner_id.tz) or pytz.utc

        # get localized dates
        if fecha:
            fecha_final =  pytz.utc.localize(datetime.datetime.strptime(fecha + ' 23:59:59', '%Y-%m-%d %H:%M:%S')).astimezone(tz)
            fecha = pytz.utc.localize(datetime.datetime.strptime(fecha + ' 00:00:00', '%Y-%m-%d %H:%M:%S')).astimezone(tz)
            
        # date_to   = pytz.utc.localize(datetime.datetime.strptime(date_to, DATETIME_FORMAT)).astimezone(tz)
        print 'aqui la fecha' + str(fecha)
        fecha=str(fecha)
        fecha_final=str(fecha_final)
        print 'aqui la fecha nueva' + str(fecha_final)
        sales = self.pool.get('sale.order')
        print sales
        sales_ids = sales.search(self.cr,self.uid,[('date_order' ,'>=' ,fecha),('date_order' ,'>=' ,fecha_final)])
        print str(sales_ids) + 'aqui ando ya en los id' #,('state','in','manual')
        res = []
        ids = []
        if fecha:
            res = sales.browse(self.cr, self.uid, sales_ids)
        return res


    def get_vouchers(self,fecha):
        # get user's timezone
        user_pool = self.pool.get('res.users')
        user = user_pool.browse(self.cr, SUPERUSER_ID, self.uid)
        tz = pytz.timezone(user.partner_id.tz) or pytz.utc
        # get localized dates
        fecha_final = pytz.utc.localize(datetime.datetime.strptime(fecha + ' 23:59:59', '%Y-%m-%d %H:%M:%S')).astimezone(tz)
        fecha = pytz.utc.localize(datetime.datetime.strptime(fecha + ' 00:00:00', '%Y-%m-%d %H:%M:%S')).astimezone(tz)
        # date_to   = pytz.utc.localize(datetime.datetime.strptime(date_to, DATETIME_FORMAT)).astimezone(tz)
        vouchers = self.pool.get('account.voucher')
        print vouchers
        vouchers_ids = vouchers.search(self.cr,self.uid,[('date' ,'>=' ,fecha),('date' ,'<=' ,fecha_final)])
        print vouchers_ids
        res = []
        ids = []
        if fecha:
            res = vouchers.browse(self.cr, self.uid, vouchers_ids)
            print res
        return res

class wrapped_report_payslip(osv.AbstractModel):
    _name = 'report.mh_account_reports.report_incomes_match_template'
    _inherit = 'report.abstract_report'
    _template = 'mh_account_reports.report_incomes_match_template'
    _wrapped_report_class = payslip_report
