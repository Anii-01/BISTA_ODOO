from odoo import models, fields

class CustomerRating(models.Model):
    _inherit = 'res.partner'

    customer_rating = fields.Selection([
        ('one_star', 'One Star'),
        ('two_star', 'Two Stars'),
        ('three_star', 'Three Stars'),
        ('four_star', 'Four Stars'),
        ('five_star', 'Five Stars')
    ], string='Customer Rating')
