# -*- coding: utf-8 -*-
# from odoo import http


# class AppStoreOdoo(http.Controller):
#     @http.route('/app__store__odoo/app__store__odoo', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/app__store__odoo/app__store__odoo/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('app__store__odoo.listing', {
#             'root': '/app__store__odoo/app__store__odoo',
#             'objects': http.request.env['app__store__odoo.app__store__odoo'].search([]),
#         })

#     @http.route('/app__store__odoo/app__store__odoo/objects/<model("app__store__odoo.app__store__odoo"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('app__store__odoo.object', {
#             'object': obj
#         })
