from reportlab.lib.utils import literal_eval
from odoo import models, fields, api


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    product_id = fields.Many2many("product.template", string="Products")

    def set_values(self):
        res = super(ResConfigSettings, self).set_values()
        self.env['ir.config_parameter'].sudo().set_param('bom_cart.product_id', self.product_id.ids)
        return res

    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        with_user = self.env['ir.config_parameter'].sudo()
        product = with_user.get_param('bom_cart.product_id')
        res.update(product_id=[(6, 0, literal_eval(product))] if product else False, )
        return res
