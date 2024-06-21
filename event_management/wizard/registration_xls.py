from odoo import models, fields, api
import xlwt
from io import BytesIO
import base64

class EventRegistrationReportWizard(models.TransientModel):
    _name = 'event.registration.report.wizard'
    _description = 'Event Registration Report Wizard'

    start_date = fields.Date(string='Start Date', required=True)
    end_date = fields.Date(string='End Date', required=True)

    #Generate Excel Report on this action 
    def generate_xls_report(self):
        registrations = self.env['event.registrations'].search([
            ('registration_date', '>=', self.start_date),
            ('registration_date', '<=', self.end_date)
        ])

        # Create an XLS file
        workbook = xlwt.Workbook(encoding='utf-8')
        worksheet = workbook.add_sheet('Event Registrations')

        # Write headers
        headers = ['Registration Date', 'Organizer Name', 'Attendee Name', 'Event Name', 'Registration State']
        for col, header in enumerate(headers):
            worksheet.write(0, col, header)

        # Write data
        row = 1
        for registration in registrations:
            worksheet.write(row, 0, registration.registration_date.strftime('%Y-%m-%d'))
            worksheet.write(row, 1, registration.event_id.organizer_id.name)
            worksheet.write(row, 2, registration.attendee_id.name)
            worksheet.write(row, 3, registration.event_id.name)
            worksheet.write(row, 4, registration.state)
            row += 1

        # Save the workbook to a BytesIO buffer
        output = BytesIO()
        workbook.save(output)
        output.seek(0)

        file_data = output.getvalue()

        attachment = self.env['ir.attachment'].create({
            'name': 'Event_Registration.xls',
            'type': 'binary',
            'datas': base64.b64encode(file_data),
            'res_model': self._name,
            'res_id': self.id
        })

        return {
            'type': 'ir.actions.act_url',
            'url': '/web/content/%s?download=true' % attachment.id,
            'target': 'new',
        }
