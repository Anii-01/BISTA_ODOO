# event_api/controllers/main.py

from odoo import http
from odoo.http import request
import json

class EventController(http.Controller):
    
    @http.route('/odoo_api', auth='none', type='json', methods=['GET'])
    def get_event_data(self,**rec):
        events = request.env['event.event'].sudo().search([])
        print("get event ----->", events)
        event_data = []
        for event in events:
            event_data.append({
                'name': event.name,
                'start_date': event.start_date.strftime('%Y-%m-%d') if event.start_date else '',
                'end_date': event.end_date.strftime('%Y-%m-%d') if event.end_date else '',
                'organizer_id': event.organizer_id.name if event.organizer_id else '',
            })
        return {'status': 200, 'response': event_data, 'message': 'Success'}
    


    @http.route('/odoo_api2', auth='none', type='json', methods=['GET'])
    def get_event_data(self,**rec):
        event_attendees = request.env['event.attendee'].sudo().search([])
        print("get event attendee ----->", event_attendees)
        event_data = []

        for event in event_attendees:
            event_data.append({
                'name': event.name,
                'email': event.email,
                'phone': event.phone,
                'user_id': event.user_id,       
            })
        return {'status': 200, 'response': event_data, 'message': 'Success'}

