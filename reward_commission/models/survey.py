# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class SurveyUserInputLine(models.Model):
    _inherit = 'survey.user_input'

    date_completed = fields.Date(string='Date Completed',index=True)
