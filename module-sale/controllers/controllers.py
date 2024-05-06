# -*- coding: utf-8 -*-
# from odoo import http


# class Module-sale(http.Controller):
#     @http.route('/module-sale/module-sale/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module-sale/module-sale/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module-sale.listing', {
#             'root': '/module-sale/module-sale',
#             'objects': http.request.env['module-sale.module-sale'].search([]),
#         })

#     @http.route('/module-sale/module-sale/objects/<model("module-sale.module-sale"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module-sale.object', {
#             'object': obj
#         })
