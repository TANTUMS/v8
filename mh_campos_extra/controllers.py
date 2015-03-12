# -*- coding: utf-8 -*-
from openerp import http

# class MhCamposExtra(http.Controller):
#     @http.route('/mh_campos_extra/mh_campos_extra/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mh_campos_extra/mh_campos_extra/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('mh_campos_extra.listing', {
#             'root': '/mh_campos_extra/mh_campos_extra',
#             'objects': http.request.env['mh_campos_extra.mh_campos_extra'].search([]),
#         })

#     @http.route('/mh_campos_extra/mh_campos_extra/objects/<model("mh_campos_extra.mh_campos_extra"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mh_campos_extra.object', {
#             'object': obj
#         })