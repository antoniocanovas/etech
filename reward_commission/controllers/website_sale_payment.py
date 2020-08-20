from odoo import fields, http, SUPERUSER_ID, tools, _
from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale
from geopy import distance


R = 50 #radius in km

class WebsiteSalePayment(WebsiteSale):
    @http.route(['/shop/payment'], type='http', auth="public", website=True, sitemap=False)
    def payment(self, **post):
        res = super(WebsiteSalePayment, self).payment()
        order = request.website.sale_get_order()
        parner_id = order.partner_id
        parner_id.geo_localize()
        hairdressers =  self._get_haidressers(parner_id)
        res.qcontext.update({'hairdressers':hairdressers})
        return res


    def _get_haidressers(self,partner_id):
        hairdressers_ids = request.env['res.partner'].sudo().search([('partner_type','=','hairdresser')])

        current_partner = (partner_id.partner_latitude, partner_id.partner_longitude)
        hairdressers = []
        for hairdresser in hairdressers_ids:
            try:
                dist = distance.distance(current_partner, (hairdresser.partner_latitude,hairdresser.partner_longitude)).km
                if (dist < R):
                    hairdressers.append({'hairdresser':hairdresser,'dist':dist})
            except ValueError:
                pass
        if hairdressers:
            hairdressers = sorted(hairdressers, key=lambda k: k['dist'])
        return hairdressers

    @http.route(['/shop/payment/transaction/',
        '/shop/payment/transaction/<int:so_id>',
        '/shop/payment/transaction/<int:so_id>/<string:access_token>'], type='json', auth="public", website=True)
    def payment_transaction(self, acquirer_id, save_token=False, so_id=None, access_token=None, token=None, **kwargs):
        res = super(WebsiteSalePayment, self).payment_transaction(acquirer_id, save_token , so_id , access_token , token, **kwargs)

        if kwargs.get('hairdresser_id'):
            if so_id:
                env = request.env['sale.order']
                domain = [('id', '=', so_id)]
                if access_token:
                    env = env.sudo()
                    domain.append(('access_token', '=', access_token))
                order = env.search(domain, limit=1)
            else:
                order = request.website.sale_get_order()
            order.hair_dresser_id = kwargs.get('hairdresser_id')
        return res
