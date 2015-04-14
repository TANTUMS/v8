# -*- coding: utf-8 -*-
from openerp import http

# class Canceller(http.Controller):
#     @http.route('/canceller/canceller/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/canceller/canceller/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('canceller.listing', {
#             'root': '/canceller/canceller',
#             'objects': http.request.env['canceller.canceller'].search([]),
#         })

#     @http.route('/canceller/canceller/objects/<model("canceller.canceller"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('canceller.object', {
#             'object': obj
#         })