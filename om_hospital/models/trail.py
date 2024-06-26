from odoo import api, fields, models, tools

class HospitalConfig(models.Model):
    _inherit = ['sale.order']
    
    confirm_user_id = fields.Many2one('res.users')

    def action_confirm(self):
        super(HospitalConfig, self).action_confirm()
        self.confirm_user_id = self.env.user.id    
    
    
class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'
    
    user = fields.Char(string="User")


