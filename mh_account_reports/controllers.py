# -*- coding: utf-8 -*-
from openerp import http

# class MhAccountReports(http.Controller):
#     @http.route('/mh_account_reports/mh_account_reports/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mh_account_reports/mh_account_reports/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('mh_account_reports.listing', {
#             'root': '/mh_account_reports/mh_account_reports',
#             'objects': http.request.env['mh_account_reports.mh_account_reports'].search([]),
#         })

#     @http.route('/mh_account_reports/mh_account_reports/objects/<model("mh_account_reports.mh_account_reports"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mh_account_reports.object', {
#             'object': obj
#         })