from odoo import models, fields

class ProductTemplateInherit(models.Model):
    _inherit = 'product.template'

    product_style_id = fields.Many2one('product.style', string='Product Style')
   
