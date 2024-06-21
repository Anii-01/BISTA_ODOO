from odoo import models, fields, api
from odoo.exceptions import UserError

class EventRegistration(models.Model):
    _name = 'event.registrations'
    _description = 'Registration'
    _rec_name = 'attendee_id'

    attendee_id = fields.Many2one('event.attendee', string='Attendee', required=True)
    event_id = fields.Many2one('event.event', string='Event', required=True)

    registration_date = fields.Datetime(string='Registration Date', default=fields.Datetime.now)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled')
    ], string='State', default='draft')


    def action_confirm(self):
        for rec in self:
            rec.state = 'confirmed'
            rec._send_registration_email()



    def action_cancel(self):
        for rec in self:
            rec.state = 'cancelled'
            rec._send_registration_email()

    #Registration Email Action
    def _send_registration_email(self):
        template = self.env.ref('event_management.email_template_registration_status')
        for registration in self:
            if not registration.attendee_id.email:
                raise UserError('Attendee has no email address.')
            if template:
                template.with_context(
                    email_to=registration.attendee_id.email,
                    email_cc=registration.event_id.organizer_id.email
                ).send_mail(registration.id, force_send=True)
