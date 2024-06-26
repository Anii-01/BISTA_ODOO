from odoo import api, fields, models, tools

class customer_inherit(models.Model):
    _inherit = ['res.partner']
    
    #delivery_days = fields.Many2many('res.users')

    day_ids = fields.Many2many('customer_inherit.dayofweek', string='Days')
    customer_id = fields.Boolean(string="customer_id")
    name = fields.Char(string='Name', required=True)
    
    # @api.onchange('customer_id')
    # def _onchange_customer_id(self):
    #     self.customer_id = self.day_ids.customer_id

        
        # if self.customer_id:
        #     supplier_rank = self.customer_id.supplier_rank or 0
        #     customer_rank = self.customer_id.customer_rank or 0
            
        #     if supplier_rank > 0 and customer_rank > 0:
        #         self.customer_type = 'Customer and Supplier'
        #     elif supplier_rank > 0:
        #         self.customer_type = 'Supplier'
        #     elif customer_rank > 0:
        #         self.customer_type = 'Customer'
        #     else:
        #         self.customer_type = 'Undefined'
        # else:
        #     self.customer_type = ''
        


            
        





