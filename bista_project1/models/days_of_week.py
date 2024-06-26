# models/day_of_week.py
from odoo import models, fields

class DayOfWeek(models.Model):
    _name = 'customer_inherit.dayofweek'
    _description = 'Day of the Week'

    name = fields.Char(string='Day', required=True)
