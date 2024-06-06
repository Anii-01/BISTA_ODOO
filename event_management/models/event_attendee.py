from odoo import fields , models, api 

class Event_Attendee(models.Model):
    _name='event.attendee'
    _description = "This handles the event attendee of company"

    name = fields.Char(string="Name", required=True)
    email = fields.Char(string="Email", required=True)

    phone = fields.Char(string="Phone")

    user_id = fields.Many2one('res.users', string="User", compute='_compute_user_id', store=True, readonly=True)

    event_ids = fields.Many2many('event.event', 'event_registration', 'attendee_id', 'event_id', string="Events")

    @api.depends('email')
    def _compute_user_id(self):
        for record in self:
            existing_user = self.env['res.users'].search([('email', '=', record.email)])

            if existing_user:
                record.user_id = existing_user.id
            else:
                # Create new user 
                new_user_vals = {
                    'name': record.name,
                    'login': record.email,  
                    'email': record.email,
                    'groups_id': [(6, 0, [])], 
                }
                new_user = self.env['res.users'].create(new_user_vals)
                record.user_id = new_user.id   