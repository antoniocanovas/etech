# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class ProductPublicCategory(models.Model):
    _inherit = "product.public.category"

    portal_only = fields.Boolean(string="Portal only")

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    portal_only = fields.Boolean(string="Portal only", compute="_compute_portal_only", store=True)

    @api.depends('public_categ_ids.portal_only')
    def _compute_portal_only(self):
        for product in self:
            product.portal_only = any(categ.portal_only for categ in self.public_categ_ids)