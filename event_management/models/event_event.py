from odoo import fields , models, api 

class Event(models.Model):
    _name='event.event'
    _description = "This handles the event management of the Company"

    name = fields.Char(string="Name")
    description = fields.Text(string="Description")
    start_date = fields.Date(string = "Start Date")
    end_date = fields.Date(string = "End Date")
    organiser_id = fields.Many2one('event.organiser' , string="Organiser")

    # attendee_ids = fields.Many2many('event.attendee' , 'event.registrations' , string= "Attendee IDs")
    
    duration = fields.Float(string="Duration", compute= '_compute_days')

    @api.depends('start_date','end_date')
    def _compute_days(self):
        for rec in self:
            if rec.start_date and rec.end_date:
                difference = (rec.end_date - rec.start_date).days
                rec.duration = difference
            else:
             rec.duration = 0  

    