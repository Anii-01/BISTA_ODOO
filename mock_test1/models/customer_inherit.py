from odoo import models,fields,api
from odoo.exceptions import ValidationError

class ValidationFormatting(models.Model):
    _inherit = 'res.partner'

    phone = fields.Char(string='Phone', size=12)  # Allow 10 digits + 2 hyphens

    @api.constrains('phone')
    def _check_phone(self):
        for record in self:
            if len(record.phone) != 12:
                raise ValidationError('Phone number must be 10 digits long.')
    
    def _format_phone(self, phone):
        if phone:
            return '{}-{}-{}{}'.format(phone[:3], phone[3:6], phone[6:9], phone[9:])
        return phone
    
    @api.onchange('phone')
    def _on_change_phone(self):
        self.phone = self._format_phone(self.phone)
        return {'value': {'phone': self.phone}}
    

    
