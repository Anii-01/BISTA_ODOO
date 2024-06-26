
import xlwt
from odoo import api, fields, models
import base64
from io import BytesIO
import io

class HospitalDoctor(models.Model):
    _name = 'hospital.doctor'
    _inherit = 'mail.thread'
    _description = 'Doctor Records'

    _rec_name = 'ref'

    name = fields.Char(string='Name', required=True)
    user_id = fields.Many2one('res.users',string='Responsible')
    gender = fields.Selection([('male','Male'),('female','Female'),('others','Others')],string = "Gender",tracking=True)
    ref = fields.Char(string="Reference",required=True)

    active = fields.Boolean(default=True)

    #def name_get(self):
    #    res=[]
     #   for rec in self:
     #       name = f'{rec.ref} - {rec.name}'
     #       res.append({rec.id, name})
     #   return res

#self is variable in odoo , which contains current record set
#all the records inside the model

   
#-------------------------------------------------------------------------------------------------------
#for server action 
    def action_doctor_xls(self):
        # Get the sale orders
        doctor_data = self.env['hospital.doctor'].browse(self.env.context.get('active_ids', []))

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
        for rec in doctor_data: 
                worksheet.write(row, 0, rec.name)
                worksheet.write(row, 1, rec.user_id.name)
                worksheet.write(row, 2, rec.ref)
                worksheet.write(row, 3, rec.gender)
        #         worksheet.write(row, 4, line.price_unit)
        #         worksheet.write(row, 5, line.price_subtotal)
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
            'res_model': 'hospital.doctor',
        })

        return {
            'type': 'ir.actions.act_url',
            'url': '/web/content/%s?download=true' % attachment.id,
            'target': 'new',
        }

#--------------------------------------------------------------------------------------------------------------------------------------
#using button
    def action_doctor_xls_button(self):
        # Get the sale orders
        #doctor_data = self.env['hospital.doctor'].browse(self.env.context.get('active_ids', []))

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
        for rec in self: 
                worksheet.write(row, 0, rec.name)
                worksheet.write(row, 1, rec.user_id.name)
                worksheet.write(row, 2, rec.ref)
                worksheet.write(row, 3, rec.gender)
        #         worksheet.write(row, 4, line.price_unit)
        #         worksheet.write(row, 5, line.price_subtotal)
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
            'res_model': 'hospital.doctor',
        })

        return {
            'type': 'ir.actions.act_url',
            'url': '/web/content/%s?download=true' % attachment.id,
            'target': 'new',
        }

    
#-----------------------------------------------------------------------------------------------

class HospitalDoctorType(models.Model):
    _name = 'hospital.doctor.type'
    _description = 'Doctor Records'
    #type = fields.Char(string="Designation",required=True)
    type = fields.Selection([('surgen','Surgen'),('dentists','Dentists'),('opd','OPD')],string="Doctor Type",tracking=True)
 