from odoo import models, fields, api

class salespersons_report(models.TransientModel):

   _name = "salespersons.report"
   _description = "salespersons report wizard"

   internal_users = fields.Many2many('res.users')

   def show_orders(self):
        self.ensure_one()
        sales_user_ids = self.internal_users.ids
        return {
            'name': 'Sale Order Lines',
            'type': 'ir.actions.act_window',
            'res_model': 'sale.order.line',
            'view_mode': 'tree,form',
            'domain': [('order_id.user_id', 'in', sales_user_ids)],
            'context': dict(self._context),
        }

      

   
