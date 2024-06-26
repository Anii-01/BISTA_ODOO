from odoo import api,fields,models

class EmailTemplate(models.Model):
    _name = 'email.template'
    _description = 'Email Template'

    _rec_name = 'ref'

    name = fields.Char(string='Name', required=True)

