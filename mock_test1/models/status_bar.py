from odoo import api,fields,models

class BistaEmployee(models.Model):
    _name = 'status.bar'
    _description = 'status bar'

    #_rec_name = 'ref'

    name = fields.Char(string='Name', required=True)
    user_id = fields.Many2one('res.users',string='Responsible')
    gender = fields.Selection([('male','Male'),('female','Female'),('others','Others')],string = "Gender",tracking=True)
    emp_role = fields.Selection([('developer','Developer'),('tester','Tester')],string="Role")
   