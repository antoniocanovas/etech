# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.http import request
from datetime import date
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT
from dateutil.relativedelta import relativedelta

DISTRIBUTOR_V = .5
HAIRDRESSE_V = 1

class ResPartner(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'

    partner_type = fields.Selection(selection=[
        ('distributor', 'Distributor'),
        ('hairdresser', 'Hairdresser')],string='Type')

    distributor_id = fields.Many2one('res.partner','Distributor')
    certification_commission = fields.Float(compute='_compute_certification_commission', string='certification commission %')

    @api.depends('distributor_id')
    def _compute_certification_commission(self):
        survey_user_input = request.env['survey.user_input']
        date_range = (date.today() - relativedelta(years=1)).strftime(DEFAULT_SERVER_DATE_FORMAT)
        certifications = survey_user_input.search([('partner_id','=',self.id),('quizz_passed','=',1),('date_completed','>', date_range )])
        if len(certifications) > 0:
            if self.partner_type == 'distributor':
                self.certification_commission = DISTRIBUTOR_V * len(certifications)

            if self.partner_type == 'hairdresser':
                self.certification_commission = HAIRDRESSE_V * len(certifications)
        else:
            self.certification_commission = 0


    def _geo_localize_all_partners(self):
        partners = self.search([()])
        for partner in partners:
            hairdresser.geo_localize()
