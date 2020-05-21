# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class ProductPublicCategory(models.Model):
    _inherit = "product.public.category"

    portal_only = fields.Boolean(string="Portal only")

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    portal_only = fields.Boolean(string="Portal only", compute="_compute_portal_only", stored=True)

    def _compute_portal_only(self):
        portal_only=False
        if any(categ.portal_only for categ in self.public_categ_ids):
            portal_only=True
        self.portal_only = portal_only