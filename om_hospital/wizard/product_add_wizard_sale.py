from odoo import api, models, fields

class ProductAddWizardSale(models.TransientModel):
    _name = "product.add.wizard.sale"
    _description = "Add product in sales quotation using Wizard"
    

    new_product_name = fields.Many2one('product.template', string="Product Name")
    new_quantity = fields.Integer(string="Quantity")

    def action_button_add_product_sales(self):
        print("This is the action button add product")
        active_id = self._context.get('active_id')
        if active_id:
            purchase_order = self.env['sale.order'].browse(active_id)
            if purchase_order:
                # Create a purchase order line...

                sale_order_line = self.env['sale.order.line'].create({
                    'order_id': purchase_order.id,
                    'product_template_id': self.new_product_name.id,
                    'product_uom_qty': self.new_quantity,
                })
             
                print("Product added to sale order line:", sale_order_line)
            else:
                print("No purchase order found in context")
        else:
            print("No active ID found in context")
