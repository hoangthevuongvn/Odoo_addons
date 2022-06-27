# -*- coding: utf-8 -*-
# from odoo import http


# class TrialReport(http.Controller):
#     @http.route('/trial_report/trial_report/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/trial_report/trial_report/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('trial_report.listing', {
#             'root': '/trial_report/trial_report',
#             'objects': http.request.env['trial_report.trial_report'].search([]),
#         })

#     @http.route('/trial_report/trial_report/objects/<model("trial_report.trial_report"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('trial_report.object', {
#             'object': obj
#         })
