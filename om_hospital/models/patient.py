from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

class HospitalPatient(models.Model):
    _name = "hospital.patient"
    #model def
    #odoo will create databse table with name hospital_patient in postgres db (postgres table)

    _inherit = "mail.thread"
    #inheriting module
    #mail module is dependent module for my module

    #model description
    #what functionality this will add
    _description = "Patient Records"  


    user_id = fields.Many2one('res.users',string='Doctor')
    name_is = fields.Char(string = 'Name',required=False, tracking=True)
    age = fields.Integer(string = "Age", tracking=True)
    is_child = fields.Boolean(string="Is Child ?", tracking=True)
    notes = fields.Text(string="Notes")
    gender = fields.Selection([('male','Male'),('female','Female'),('others','Others')],string="Gender", tracking=True)
    #capitalized_name = fields.Char(string='Capitalized Name')
    #capitalized_name = fields.Char(string='Capitalized Name',compute='_compute_capitalized_name')
    #after adding compute = field become read only field
    #readonly = False in python , = 0 in xml  if want to make field editable..
    capitalized_name = fields.Char(string='Capitalized Name',compute='_compute_capitalized_name',store=True)
    #bydefault the compute field is storing any value in db , to store in db :  store = True

    ref = fields.Char(string="Reference",default=lambda self:_('New'))

    #many-to-one
    doctor_id = fields.Many2one('hospital.doctor',string="Doctor")
    #many-to-many
    tag_ids = fields.Many2many('res.partner.category','hospital_patient_tag_rel','patient_id','tag_id',string="Tags")

    
    #decorator , it has to be triggered on change
    #whenever the value of the filed 'age' is change this function will triggere
    @api.onchange('age') #at api onchange which field have to change.. or on multiple fields  also
    #self - is a record set .. by which we can get all the fields
    def _onchange_age(self):
        if self.age <= 10:
            self.is_child = True
        else:
            self.is_child = False

    @api.depends('name_is')  #at the run time changes will happens..
    def _compute_capitalized_name(self):
        self.capitalized_name = 'Test'

        for rec in self:
            if self.name_is:
                rec.capitalized_name = self.name_is.upper()
            else:
                rec.capitalized_name = ""


    @api.constrains('is_child','age')
    def _check_child_age(self):
        for rec in self:
            if rec.is_child == True and rec.age == 0:
                raise ValidationError(_("Age has to be recorded!"))


    #inheriting the create method for our own customization   
    @api.model_create_multi
    def create(self,vals_list):
        for vals in vals_list:
            vals['ref'] = self.env['ir.sequence'].next_by_code('hospital.patient')
        return super(HospitalPatient,self).create(vals_list)
    

    def name_get(self):
        result = []
        for record in self:
            name = f"{record.name_is}"
            result.append((record.id, name))
        return result
    
    #Customised name_get
    #@api.multi
    # def name_get(self):
    #     result = []
    #     for rec in self:
    #         name = rec.name_is + ' - [' + str(rec.age) + ']'
    #         result.append((rec.id, name)) #rec_id & its value
    #     return result
    
    def _name_search(self, name='', args=None, operator='ilike', limit=100):
        if args is None:
            args = []
        domain = args + ['|', ('name_is', operator, name), ('age', operator, name)]
        return super(HospitalPatient, self)._search(domain, limit=limit, access_rights_uid=self.env.uid)


    def name_get(self):
            result = []
            for record in self:
                name = f"{record.name_is}"
                result.append((record.id, name))
            return result
    
   