from odoo import api,fields,models

class Product_Style(models.Model):
    _name = 'product.style'

    _description = 'The Product styles'

    name = fields.Char(string='Name', required=True)
    code = fields.Integer(string = "Code", unique=True)

    priority = fields.Selection([
            ('0', 'Normal'),
            ('1', 'Low'),
            ('2', 'High'),
            ('3', 'Very High')], string="Priority") # used to order
