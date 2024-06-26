from odoo import models, fields, api

class SmartbuttonContactOrderline(models.Model):
    _inherit = 'res.partner'

    orderline_count = fields.Integer(compute='_compute_orderline_count')

    @api.depends('sale_order_ids.order_line')
    def _compute_orderline_count(self):
        for partner in self:
            partner.orderline_count = self.env['sale.order.line'].search_count([('order_id.partner_id', '=', partner.id)])

    def action_view_orderline(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Sale Order Lines',
            'view_mode': 'tree,form',
            'res_model': 'sale.order.line',
            'domain': [('order_id.partner_id', '=', self.id)],
            'context': dict(self._context),
        }
