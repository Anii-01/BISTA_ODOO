
import xlwt
from odoo import api, fields, models
import base64
from io import BytesIO
import io

class sale_order_xls_report(models.Model):
    # _name = "sale.order.xls.report"
    _description = "sale order xls report"

    _inherit = ['sale.order']

    
    # def generate_excel_product(self):
        
    #     print("XLS REPORT Printing...")

    def generate_excel_product(self):
        # Create the Excel workbook and worksheet
        workbook = xlwt.Workbook()
        worksheet = workbook.add_sheet('Product Information')

        # Write the report title
        title_style = xlwt.easyxf('font: bold on; align: horiz center;')
        worksheet.write_merge(0, 0, 0, 5, 'Product Information Report', title_style)
        worksheet.write(1, 0, 'Quotation Number', xlwt.easyxf('font: bold on;'))
        worksheet.write(1, 1, self.name)

        # Write the headers for the product data
        worksheet.write(3, 0, 'Product Number', xlwt.easyxf('font: bold on;'))
        worksheet.write(3, 1, 'Quantity', xlwt.easyxf('font: bold on;'))
        worksheet.write(3, 2, 'Unit Price', xlwt.easyxf('font: bold on;'))
        worksheet.write(3, 3, 'Sub Total', xlwt.easyxf('font: bold on;'))

        # Write the product data
        row = 4
        for order in self:
            for line in order.order_line:
                worksheet.write(row, 0, line.product_id.default_code or line.product_id.name)
                worksheet.write(row, 1, line.product_uom_qty)
                worksheet.write(row, 2, line.price_unit)
                worksheet.write(row, 3, line.price_subtotal)
                row += 1

        # Save the report file
        report_file = BytesIO()
        workbook.save(report_file)
        report_file.seek(0)

        filename = 'Product Information Report.xls'
        attachment = self.env['ir.attachment'].create({
            'name': filename,
            'datas': base64.encodebytes(report_file.read()),
            'res_model': self._name,
            'res_id': self.id
        })

        return {
            'type': 'ir.actions.act_url',
            'url': '/web/content/%s?download=true' % attachment.id,
            'target': 'new',
        }

    #for the send by mail..(Custome mail.. embending the custome url link)

    # @api.depends('name')
    # def _compute_customer_preview_link(self):
    #     base_url = self.env['ir.config_parameter'].sudo().get_param('web.base.url')
    #     for order in self:
    #         order.customer_preview_link = f"{base_url}/my/orders/{order.name.split('S')[1]}"

    # customer_preview_link = fields.Char("Customer Preview Link", compute='_compute_customer_preview_link', store=True)


    #for action 
    def action_export_sale_order_xls(self):
        # Get the sale orders
        sale_orders = self.env['sale.order'].browse(self.env.context.get('active_ids', []))

        # Create the Excel workbook and worksheet
        workbook = xlwt.Workbook()
        worksheet = workbook.add_sheet('Sale Orders')

        # Write the report title
        title_style = xlwt.easyxf('font: bold on; align: horiz center;')
        worksheet.write_merge(0, 0, 0, 5, 'Sale Order Report', title_style)

        # Write the headers for the sale order line data
        header_style = xlwt.easyxf('font: bold on; align: horiz center;')
        headers = ['Order Name', 'Product', 'Description', 'Quantity', 'Unit Price', 'Subtotal']
        for col_num, header in enumerate(headers):
            worksheet.write(1, col_num, header, header_style)

        # Write the sale order line data
        row = 2
        for order in sale_orders:
            for line in order.order_line:
                worksheet.write(row, 0, order.name)
                worksheet.write(row, 1, line.product_id.name)
                worksheet.write(row, 2, line.name)
                worksheet.write(row, 3, line.product_uom_qty)
                worksheet.write(row, 4, line.price_unit)
                worksheet.write(row, 5, line.price_subtotal)
                row += 1

        # Save the report file
        report_file = io.BytesIO()
        workbook.save(report_file)
        report_file.seek(0)

        filename = 'Sale_Order_Report.xls'
        attachment = self.env['ir.attachment'].create({
            'name': filename,
            'type': 'binary',
            'datas': base64.b64encode(report_file.getvalue()),
            'store_fname': filename,
            'mimetype': 'application/vnd.ms-excel',
            'res_model': 'sale.order',
        })

        return {
            'type': 'ir.actions.act_url',
            'url': '/web/content/%s?download=true' % attachment.id,
            'target': 'new',
        }
    
    

    
