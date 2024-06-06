from odoo import models, api

class SendEmailConfirm(models.Model):
    _inherit = 'sale.order'

    def action_confirm(self):
        # super for exsting..
        res = super(SendEmailConfirm, self).action_confirm()

        #action_confirm
        
        # email sending
        # template_id = self.env.ref('sale.email_template_edi_sale').id
        # for order in self:
        #     if order.partner_id.email:
        #         email_values = {
        #             'email_to': order.partner_id.email,
        #             'auto_delete': False,
        #         }
        #         self.env['mail.template'].browse(template_id).send_mail(order.id, email_values=email_values, force_send=True)
        
        # return res
    