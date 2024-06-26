from odoo import api, models, fields

class ProductCategorySearch(models.Model):
    _inherit = 'product.template'

    def name_get(self):
        res = super(ProductCategorySearch, self).name_get()
        result = []
        for product_id, name in res:
            product = self.browse(product_id)
            if product.categ_id:
                name = '%s [%s]' % (name, product.categ_id.name)
            result.append((product_id, name))
        return result
    
    @api.model
    def _name_search(self, name='', args=None, operator='ilike', limit=100, name_get_uid=None):
        args = args or []
        domain = []
        if name:
            domain = ['|', ('name', operator, name + '%'), ('categ_id', operator, name + '%')]
        return super(ProductCategorySearch, self)._search(domain + args, limit=limit, access_rights_uid=name_get_uid)
    
    