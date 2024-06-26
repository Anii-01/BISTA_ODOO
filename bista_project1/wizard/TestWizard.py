import datetime
from odoo import models, fields, api

class TestWizard(models.TransientModel):

   _name = "test.wizard"
   _description = "Create Appointment Wizard"


   name = fields.Char(string = 'Name',required=False)
   employee_id = fields.Integer(string="Emp_id", required=True)
   product = fields.Many2one('product.product',string = 'Products')


   def action_create_wizard(self):
        print("Button is clicked!")
        pass
   
   #for printing the active ids by python side...
   @api.model
   def default_get(self,fields):
       res = super(TestWizard,self).default_get(fields)
       #res['date_cancel'] = datetime.date.today()

       print("--------------------------------------------------")
       print("-----Context--------",self.env.context)
       if self.env.context.get('active_id'):
         res['employee_id'] = self.env.context.get('active_id')
       return res
   
   #using  'self.env.context'  we can retrive the context