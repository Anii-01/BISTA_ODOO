from odoo import api, fields, models, _
import xlwt
import base64
import io

class SaleReportWizard(models.TransientModel):
    _name = "appointment.report.wizard"
    _description = "Sale_Order report wizard"

    customer_id = fields.Many2one("res.partner", string="Customer")
    date_from = fields.Date(string="Date From")
    date_to = fields.Date(string="Date to")

#For PDF Report

    def action_print_report(self):
        domain = []
        customer_id=self.customer_id

        if self.customer_id:
            domain += [('partner_id', '=', self.customer_id.id)]

        date_from = self.date_from

        if self.date_from:
            domain += [('create_date', '>=', date_from)]

        date_to=self.date_to

        if self.date_to:
            domain += [('expected_date', '<=', date_to)]

        quotations = self.env["sale.order"].search_read(domain)

        data = {
            'form': self.read()[0],
            'quotations': quotations
        }

        # Make sure the XML ID 'hosp_manag_sys.action_report_quotations' exists
        action = self.env.ref('om_hospital.om_hospital_report_optional_product')
        if action:
            return action.report_action(self, data=data)
        else:
            return {'error': 'Action not found'}
    


#Task-2 : Excel Report

    def action_print_excel(self):
        print("XLS REPORT Printing...")

    
    def action_print_excel(self):
        # Get the quotations for the selected criteria
        domain = []
        if self.customer_id:
            domain += [('partner_id', '=', self.customer_id.id)]
        if self.date_from:
            domain += [('create_date', '>=', self.date_from)]
        if self.date_to:
            domain += [('create_date', '<=', self.date_to)]
        quotations = self.env["sale.order"].search(domain)

        # Create the Excel workbook and worksheet
        workbook = xlwt.Workbook()
        worksheet = workbook.add_sheet('Quotations Sheet')

        # Write the report title
        title_style = xlwt.easyxf('font: bold on; align: horiz center;')
        worksheet.write_merge(0, 0, 0, 1, 'Quotation Sheet Report', title_style)
        worksheet.write_merge(1, 1, 0, 1, 'Customer:', xlwt.easyxf('font: bold on;'))
        worksheet.write_merge(1, 1, 2, 2, self.customer_id.name if self.customer_id else '')
        worksheet.write_merge(2, 2, 0, 1, 'Date From:', xlwt.easyxf('font: bold on;'))
        worksheet.write_merge(2, 2, 2, 2, str(self.date_from) if self.date_from else '')
        worksheet.write_merge(3, 3, 0, 1, 'Date To:', xlwt.easyxf('font: bold on;'))
        worksheet.write_merge(3, 3, 2, 2, str(self.date_to) if self.date_to else '')

        # Write the headers for the quotation data
        header_style = xlwt.easyxf('font: bold on; align: horiz center;')
        worksheet.write(5, 0, 'Reference', header_style)
        worksheet.write(5, 1, 'Amount', header_style)
        

        # Write the quotation data
        row = 6
        sum=0
        for quotation in quotations:
            worksheet.write(row, 0, quotation.name)
            worksheet.write(row, 1, quotation.amount_total)
            
            sum+=quotation.amount_total
            row += 1
        worksheet.write(row, 0, "Sum")
        worksheet.write(row, 1, sum)

        # Save the report file
        report_file = io.BytesIO()
        workbook.save(report_file)
        report_file.seek(0)

        filename = 'Quotation Sheet Report.xls'
        attachment = self.env['ir.attachment'].create({
            'name': filename,
            'datas': base64.encodebytes(report_file.getvalue()),
            'res_model': self._name,
            'res_id': self.id
        })

        return {
            'type': 'ir.actions.act_url',
            'url': '/web/content/%s?download=true' % attachment.id,
            'target': 'new',
        }