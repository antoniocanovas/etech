# -*- coding: utf-8 -*-
from odoo import api, fields, models, _

class ResPartner(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'

    partner_type = fields.Selection(selection=[
        ('distributor', 'Distributor'),
        ('hairdresser', 'Hairdresser')],string='Type')

    distributor_id = fields.Many2one('res.partner','Distributor')
    certification_commission = fields.Float(compute='_compute_certification_commission', string='certification commission')

    #@api.depends('public_categ_ids.portal_only')
    def _compute_certification_commission(self):
        self.certification_commission = 4
