from odoo.addons.portal.controllers.portal import CustomerPortal
from odoo.http import request

from odoo import http

class EventPortal(CustomerPortal):

    def _prepare_home_portal_values(self, counters):
        print("-----counters--------", counters)
        rtn = super()._prepare_home_portal_values(counters)
        print("_prepare_home_portal_values called...")
        current_user = request.env.user.partner_id
        if 'event_count' in counters:
            rtn['event_count']  = request.env['event.event'].search_count([('portal_user', '=', current_user.id)])
        print(rtn)
        
        return rtn
    
#controller
    # @http.route(['/my/events'],type='http',website=True)
    # def EventPortal_ListView(self,**kw):
    #     print("Hello you called /my/students controller...")
    #     event_obj = request.env['event.event']
    #     events = event_obj.search([])
    #     vals = {'events': events, 'page_name':'my_details1'}
    #     return request.render("event_management.event_list_view_portal",vals)
    #     #dict as a context

#controller for list_view
    @http.route(['/my/events'], type='http', website=True, auth='user')
    def EventPortal_ListView(self, **kw):
        print("Hello, you called /my/events controller...")
        
        current_user = request.env.user.partner_id
        
        # Fetch events related to the current user's partner
        event_obj = request.env['event.event']
        events = event_obj.search([('portal_user', '=', current_user.id)])
        
        vals = {
            'events': events,
            'page_name': 'my_details1'
        }
        return request.render("event_management.event_list_view_portal", vals)


#controller for form_view 
    @http.route(["/my/event/<model('event.event'):event>"], type="http", website=True, auth="public")
    def EventPortal_FormView(self, event):
        print("Controller for form view calling...")
        vals = {"event": event, "page_name": "event_form_view"}
        
        return request.render("event_management.event_form_view_portal", vals)
    
    
# #controller for button confirm
#     @http.route('/my/event/confirm/<int:event_id>', type='http', auth="user", website=True)
#     def confirm_registration(self, event_id, **kw):
#         event = request.env['event.event'].sudo().browse(event_id)
#         if event:
#             event.action_confirm()
#         return request.redirect('/my/events')
    
 #controller for button confirm
    @http.route('/my/event/confirm/<int:event_id>', type='http', auth="user", website=True)
    def confirm_registration(self, event_id, **kw):
        event = request.env['event.event'].sudo().browse(event_id)
        if event.exists():
            event.action_confirm()
        return request.redirect('/my/events')

    @http.route('/my/event/cancel/<int:event_id>', type='http', auth="user", website=True)
    def cancel_registration(self, event_id, **kw):
        event = request.env['event.event'].sudo().browse(event_id)
        if event.exists():
            event.action_cancel()
        return request.redirect('/my/events')

    @http.route('/my/event/draft/<int:event_id>', type='http', auth="user", website=True)
    def draft_registration(self, event_id, **kw):
        event = request.env['event.event'].sudo().browse(event_id)
        if event.exists():
            event.action_draft()
        return request.redirect('/my/events')
    
    
#controller for report
    @http.route('/my/event/print/<model("event.event"):event_id>', type='http', auth="user", website=True)
    def EventPortal_report(self, event_id, **kw):
        print("this is report printing controller....,",event_id.name)
        return self._show_report(model=event_id,report_type='pdf',report_ref="event_management.report_generate_event_details", download=True)
    


#website ----------------------------------------------------------------------------------------------------------------

#even.event
#controller for website
    @http.route(['/event/registration'], type='http', website=True, auth='user')
    def EventPort_forWebsite(self, **kw):
        print("menu controller called...")
        organizers = request.env['event.organizer'].sudo().search([])
        attendees = request.env['event.organizer'].sudo().search([])
        return http.request.render("event_management.create_event_form",{
            'organizers': organizers,
            'attendees': attendees,})
    

    @http.route(['/create_event/registration'], type='http', website=True, auth='user')
    def EventPort_forWebsite_form(self, **kw):
        print("data received....",kw)
        request.env['event.event'].sudo().create(kw)
        return http.request.render("event_management.thanks_event_form",{})
    