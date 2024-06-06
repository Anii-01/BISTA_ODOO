from odoo import fields , models, api 

class Registrations(models.Model):
    _name='event.registrations'
    _description = "This handles the Registration of the Event"

    attendee_id = fields.Many2one('event.attendee' , string="Attendee ID")
    event_id = fields.Many2one('event.event' , string="Event ID")
    registration_date = fields.Date(string = "Registration Date")

    
    # state = fields.Selection([('draft','Draft'),('confirm','Confirm'),
    #                              ('cancelled','Cancelled')],string="State")
    
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled')], string='Status', default='draft')

    
    def action_confirm(self):
        self.state = "confirmed"

    def action_cancel(self):
        self.state = "cancelled"