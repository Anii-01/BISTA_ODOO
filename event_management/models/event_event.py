from odoo import models, fields, api
from datetime import datetime

class EventEvent(models.Model):
    _name = 'event.event'
    _description = 'Event'
    rec_name = 'name'

    portal_user = fields.Many2one('res.partner',string='Partner')
    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    start_date = fields.Datetime(string='Start Date')
    end_date = fields.Datetime(string='End Date')

    organizer_id = fields.Many2one('event.organizer', string='Organizer')

    attendee_ids = fields.Many2many('event.attendee', 'event_registration', 'event_id', 'attendee_id', string='Attendees')
    duration = fields.Float(string='Duration (days)', compute='_compute_duration', store=True)
    attendee_count = fields.Integer(string='Attendee Count', compute='_compute_attendee_count', store=True)

    @api.depends('start_date', 'end_date')
    def _compute_duration(self):
        for event in self:
            if event.start_date and event.end_date:
                val = event.end_date - event.start_date
                event.duration = val.days + (val.seconds / 86400)
            else:
                event.duration = 0

    #Calulating the number of attendees registered
    @api.depends('attendee_ids')
    def _compute_attendee_count(self):
        for event in self:
            event.attendee_count = len(event.attendee_ids)

    #Smart Button Action
    def action_view_attendees(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Attendees',
            'view_mode': 'tree',
            'res_model': 'event.attendee',
            'domain': [('id', 'in', self.attendee_ids.ids)],
            'context': {'default_event_ids': [(6, 0, [self.id])]},
        }
    
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled')
    ], string='State', default='draft')

    def action_confirm(self):
        for rec in self:
            rec.state = 'confirmed'

    def action_cancel(self):
        for rec in self:
            rec.state = 'cancelled'

    def action_draft(self):
        for rec in self:
            rec.state = 'draft'

    def _get_report_base_filename(self):
        self.ensure_one()
        return 'Event %s' % (self.name)