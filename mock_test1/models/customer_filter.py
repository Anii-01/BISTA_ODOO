from odoo import fields , models, api 

class CustomerRating(models.Model):
    _inherit = ['res.partner']

    filter_pricelist = fields.Boolean(string="Filter Products in SO Based on Pricelist " ,default = True)


class SaleOrderLineFilterProducts(models.Model):
    _inherit = 'sale.order.line'

    @api.onchange('order_id.partner_id')
    def _onchange_partner_id(self):
        if self.order_id.partner_id.filter_pricelist:
            self.product_id = False
            return {'domain': {'product_id': self._get_pricelist_filtered_products()}}
        return {'domain': {'product_id': []}}

    def _get_pricelist_filtered_products(self):
        partner = self.order_id.partner_id
        if not partner or not partner.property_product_pricelist:
            return [('id', 'in', [])]

        pricelist = partner.property_product_pricelist
        item_ids = pricelist.item_ids.filtered(lambda i: i.applied_on == '1_product' and i.product_id).mapped('product_id').ids
        return [('id', 'in', item_ids)]