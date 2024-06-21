from odoo import http
from odoo.http import request

class Event_Organizer(http.Controller):
    @http.route('/event/',website=True,auth='public')
    def event_organizer(self,**kw):
        return "Hello"
        #return request.render("event_organizer",{})