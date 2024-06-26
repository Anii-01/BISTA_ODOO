from odoo import api,fields,models

class BistaEmployee(models.Model):
    _name = 'bista.employee'
    _description = 'Bista Employees Details'

    _rec_name = 'name'

    name = fields.Char(string='Name', required=True)
    user_id = fields.Many2one('res.users',string='Responsible')
    gender = fields.Selection([('male','Male'),('female','Female'),('others','Others')],string = "Gender",tracking=True)
    emp_role = fields.Selection([('developer','Developer'),('tester','Tester')],string="Role")

    order_line = fields.One2many('res.users','user_id', string="Order Lines")


    state = fields.Selection([
        ('new','New'),
        ('received','Offer Received'),
        ('accepted','Offer Accepted'),     
        ('sold','Sold'),
        ('cancel','Canceled')
        ],
         default='new',string="Status")
   

    #def name_get(self):
    #    res=[]
     #   for rec in self:
     #       name = f'{rec.ref} - {rec.name}'
     #       res.append({rec.id, name})
     #   return res

#self is variable in odoo , which contains current record set
#all the records inside the model


    def action_create_wizard_from_button(self):
       action = self.env.ref('bista_project1.action_create_wizard').read()[0]
       return action
    
    def action_sold(self):
        self.state = "sold"

    def action_cancel(self):
        self.state = "cancel"

    def action_approve(self):
        pass


