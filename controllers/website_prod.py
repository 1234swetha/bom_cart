from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale


class WebsiteSale(WebsiteSale):
    def cart(self, access_token=None, revive='', **post):
        values = super().cart(access_token=access_token, revive=revive, **post)
        product = eval(request.env['ir.config_parameter'].sudo().get_param('bom_cart.product_id'))
        values.qcontext.update({
            'bom': product,
        })
        return values
