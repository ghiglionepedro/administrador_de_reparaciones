# -*- coding: utf-8 -*-
# from odoo import http


# class Nahe-custom(http.Controller):
#     @http.route('/nahe-custom/nahe-custom', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/nahe-custom/nahe-custom/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('nahe-custom.listing', {
#             'root': '/nahe-custom/nahe-custom',
#             'objects': http.request.env['nahe-custom.nahe-custom'].search([]),
#         })

#     @http.route('/nahe-custom/nahe-custom/objects/<model("nahe-custom.nahe-custom"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('nahe-custom.object', {
#             'object': obj
#         })
