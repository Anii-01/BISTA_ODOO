from odoo import api, models, fields

class ProductAddWizard(models.TransientModel):
    _name = "product.add.wizard"
    _description = "Add product in quotation using Wizard"
    

    new_product_name = fields.Many2one('product.product', string="Product Name")
    new_quantity = fields.Integer(string="Quantity")
    purchase_id = fields.Integer(string="Purchase Id")

    def action_button_add_product(self):
        print("This is the action button add product")
        active_id = self._context.get('active_id')
        if active_id:
            purchase_order = self.env['purchase.order'].browse(active_id)
            if purchase_order:
                # Create a purchase order line...

                purchase_order_line = self.env['purchase.order.line'].create({
                    'order_id': purchase_order.id,
                    'product_id': self.new_product_name.id,
                    'product_qty': self.new_quantity,
                })
             
                print("Product added to purchase order line:", purchase_order_line)
            else:
                print("No purchase order found in context")
        else:
            print("No active ID found in context")
