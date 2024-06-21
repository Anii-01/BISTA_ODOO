from odoo import models, fields, api

class EventOrganizer(models.Model):
    _name = 'event.organizer'
    _description = 'Organizer'

    name = fields.Char(string='Name', required=True)

    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')

    user_id = fields.Many2one('res.users', string='User', readonly=True)
    event_ids = fields.One2many('event.event', 'organizer_id', string='Events')

    # def create(self, vals):
        
    #     # Automatically create a user when an organizer is created
    #     user_vals = {
    #         'name': vals.get('name'),
    #         'login': vals.get('email'),
    #         'email': vals.get('email'),
    #     }
    #     user = self.env['res.users'].create(user_vals)
    #     vals['user_id'] = user.id
    #     return super(EventOrganizer, self).create(vals)
    
    # def create(self, vals):
    #     # Create the event.organizer record
    #     res = super(EventOrganizer, self).create(vals)
    #     print(res)
    #     # Automatically create a user when an Organizer is created
    #     user_vals = {
    #         'name': res.name,
    #         'login': res.email,
    #         'email': res.email,
    #     }
    #     user = self.env['res.users'].create(user_vals)
        
    #     # Assign the created user to the organizer
    #     res.user_id = user.id

    #     return res

