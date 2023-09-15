# -*- coding: utf-8 -*-
# from odoo import http


# class L10nMro(http.Controller):
#     @http.route('/l10n_mro/l10n_mro', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/l10n_mro/l10n_mro/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('l10n_mro.listing', {
#             'root': '/l10n_mro/l10n_mro',
#             'objects': http.request.env['l10n_mro.l10n_mro'].search([]),
#         })

#     @http.route('/l10n_mro/l10n_mro/objects/<model("l10n_mro.l10n_mro"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('l10n_mro.object', {
#             'object': obj
#         })
