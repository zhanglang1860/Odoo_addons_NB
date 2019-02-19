# -*- coding: utf-8 -*-
from odoo import http

# class Autocrword(http.Controller):
#     @http.route('/autocrword/autocrword/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/autocrword/autocrword/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('autocrword.listing', {
#             'root': '/autocrword/autocrword',
#             'objects': http.request.env['autocrword.autocrword'].search([]),
#         })

#     @http.route('/autocrword/autocrword/objects/<model("autocrword.autocrword"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('autocrword.object', {
#             'object': obj
#         })