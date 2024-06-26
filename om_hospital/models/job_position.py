from odoo import api, fields, models

class CustomerNameSearch(models.Model):
    _inherit = 'res.partner'

    @api.model
    def _name_search(self, name='', args=None, operator='ilike', limit=100, name_get_uid=None):
        args = args or []
        domain = []
        if name:
            domain = ['|', ('function', operator, name + '%'), ('name', operator, name + '%')]
        return super(CustomerNameSearch, self)._search(domain + args, limit=limit, access_rights_uid=name_get_uid)
