# -*- coding: utf-8 -*-
from openerp import http

# class MhZonas(http.Controller):
#     @http.route('/mh_zonas/mh_zonas/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mh_zonas/mh_zonas/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('mh_zonas.listing', {
#             'root': '/mh_zonas/mh_zonas',
#             'objects': http.request.env['mh_zonas.mh_zonas'].search([]),
#         })

#     @http.route('/mh_zonas/mh_zonas/objects/<model("mh_zonas.mh_zonas"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mh_zonas.object', {
#             'object': obj
#         })