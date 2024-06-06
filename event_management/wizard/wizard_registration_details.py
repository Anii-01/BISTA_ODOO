from odoo import models, fields, api

class Registration_details(models.TransientModel):

   _name = "Registration_details"
   _description = "Registration_details wizard"


   def show_orders(self):
        self.ensure_one()
        sales_user_ids = self.internal_users.ids
        return {
            'name': 'Registraion details',
            'type': 'ir.actions.act_window',
            'res_model': 'event.registrations',
            'view_mode': 'tree,form',
            'domain': [('order_id.user_id', 'in', sales_user_ids)],
            'context': dict(self._context),
        }

      

   
