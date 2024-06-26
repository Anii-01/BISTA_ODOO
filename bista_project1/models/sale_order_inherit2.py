from odoo import api, fields, models
from lxml import etree

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    confirm_user_id = fields.Many2one('res.users', string='Confirmed User')
    Customer_Country = fields.Many2one('res.country', string='Customer Country')

    delivery_day = fields.Many2one('customer_inherit.dayofweek', string='Delivery Day')
    partner_day_ids = fields.Many2many(related='partner_id.day_ids', string='Available Delivery Days')

    @api.onchange('partner_id')
    def _onchange_partner_id(self):
        if self.partner_id:
            # Clear previous selection
            self.delivery_day = False
            # Set domain for delivery_days field based on partner's delivery_days_ids
            domain = [('id', 'in', self.partner_id.day_ids.ids)]
            return {'domain': {'delivery_day': domain}}
        else:
            # Clear selection and domain if no partner is set
            self.delivery_day = False
            return {'domain': {'delivery_day': []}}
    
    @api.model
    def fields_view_get(self, view_id=None, view_type='form', toolbar=False, submenu=False):
        res = super(SaleOrder, self).fields_view_get(view_id, view_type, toolbar, submenu)
        if view_type == 'form':
            doc = etree.XML(res['arch'])
            for node in doc.xpath("//field[@name='delivery_day']"):
                node.set('domain', "[('id', 'in', partner_day_ids)]")
            res['arch'] = etree.tostring(doc, encoding='unicode')
        return res
    
    def check_orm(self):
        pass

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'
    
    user = fields.Char(string="User")
