from odoo import api, fields, models, tools

class Customer_Rating(models.Model):
    _inherit = ['sale.order']
    #confirm_user_id = fields.Many2one('res.users')
    
    priority = fields.Selection([
            ('0', 'Normal'),
            ('1', 'Low'),
            ('2', 'High'),
            ('3', 'Very High')], string="Priority") # used to order

'''
    
class ProductMaster(models.Model):
    _name = 'product.master'
    _description = 'Product Master'

    name = fields.Char(string='Product Name', required=True)
    color = fields.Char(string='Color')

class BranchProductData(models.Model):
    _name = 'branch.product.data'
    _description = 'Branch Product Data'
    _inherit = 'product.template'

    branch_name = fields.Char(string='Branch Name')

'''