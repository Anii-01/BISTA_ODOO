from odoo import models,fields,api

class Productstyle(models.Model):
    _name= 'product.style'
    _description='Product Style'

    name = fields.Char(string="Name",required="true")
    code = fields.Char(string="Code",required="true")

    _sql_constraints = [
        ('code_unique', 'unique(code)', 'The code must be unique!'),
    ]

