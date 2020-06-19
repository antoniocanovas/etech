# -*- coding: utf-8 -*-
from odoo import api, fields, models, _

class SaleOrder(models.Model):
    _inherit = "sale.order"

    hair_dresser_id = fields.Many2one('res.partner','Hairdresser')
