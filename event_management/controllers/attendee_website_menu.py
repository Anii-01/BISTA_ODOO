from odoo.addons.portal.controllers.portal import CustomerPortal
from odoo.http import request

from odoo import http

class EventAttendeeMenu(CustomerPortal):

#controller for attendee
    @http.route(['/event/attendee_registration'], type='http', website=True, auth='user')
    def Attendee_Registration_form(self, **kw):
        print("Attendee_Registration controller called...")
        attendees = request.env['event.attendee'].sudo().search([])
        attendee_names = attendees.mapped('name') 

        events =  request.env['event.event'].sudo().search([])
        event_names = events.mapped('name')

        return http.request.render("event_management.create_event_attendee_form",{'attendees': attendee_names,'event_names':event_names})
    

    @http.route(['/create_attendee/attendee_registration'], type='http', website=True, auth='user')
    def Create_Attendee_Registration_(self, **kw):
        print("attendee data received....",kw)
        request.env['event.attendee'].sudo().create(kw)
        return http.request.render("event_management.thanks_event__attendee_form",{})
    

