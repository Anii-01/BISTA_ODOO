from odoo import models, fields,api

class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _description = 'Hospital Appointments'

    name = fields.Char(string="Appointment Type", required=True)
    patient_id = fields.Many2one('hospital.patient', string="Patient", required=True)
    doctor_id = fields.Many2one('hospital.doctor', string="Doctor", required=True)
    appointment_date = fields.Datetime(string="Appointment Date", required=True)
    # Add more fields as needed

   
    priority = fields.Selection([
            ('0', 'Normal'),
            ('1', 'Low'),
            ('2', 'High'),
            ('3', 'Very High')], string="Priority") # used to order



