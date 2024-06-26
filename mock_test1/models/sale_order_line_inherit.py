from odoo import models, fields, api

class SaleOrderLineInherit(models.Model):
    _inherit = 'sale.order.line'

    product_style_id = fields.Many2one('product.style', string='Product Style')

    @api.onchange('product_template_id')
    def onchange_product_id(self):
        if self.product_template_id:
            self.product_style_id = self.product_template_id.product_style_id.id
        else:
            self.product_style_id = False


