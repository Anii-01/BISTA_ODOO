from odoo import api, fields, models, _


class CreateAppointmentWiz(models.TransientModel):
    #not stored data in database , it is for temporary purpose 
    _name = "create.appointment.wizard"
    _description = "Create Appointment Wizard"
   
   
    name = fields.Char(string = 'Name',required=False)
    patient_id = fields.Many2one('hospital.patient',string = "Patient",required=True)


    product = fields.Many2one('product.product',string = 'Products')

    patient = fields.Many2one('hospital.patient',string = "Patient_tags")



   

    def action_create_appointment(self):
        print("Button is clicked!")
        pass