from odoo import models, fields

class ProductManufacturer(models.Model):
    _name = 'product.manufacturer'
    _description = 'Product Manufacturer'
    _order = 'name'
    
    # Name: Char field, Mandatory, Indexed
    name = fields.Char(string='Name', required=True, index=True)

    # Address fields
    street_name = fields.Char(string='Street Name')
    building = fields.Char(string='Building')
    floor_room_number = fields.Char(string='Floor/Room #')
    street2 = fields.Char(string='Street 2')
    city = fields.Char(string='City')
    zip = fields.Char(string='ZIP')
    phone = fields.Char(string='Phone')
    email = fields.Char(string='Email')

    # State and Country as Many2one relation to default state and country
    state_id = fields.Many2one('res.country.state', string='State')
    country_id = fields.Many2one('res.country', string='Country')
