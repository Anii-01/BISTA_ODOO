from odoo import api, fields, models

class ResGroups(models.Model):
    _inherit = 'res.groups'

    @api.model
    def create_groups(self):
        # Create Event Manager group
        event_manager_group = self.create({
            'name': 'Event Manager',
            'implied_ids': [(6, 0, [])],
            'category_id': self.env.ref('base.module_category_hidden').id,
        })

        # Create Organizer group
        organizer_group = self.create({
            'name': 'Organizer',
            'implied_ids': [(6, 0, [])],
            'category_id': self.env.ref('base.module_category_hidden').id,
        })

        # Create Attendee group
        attendee_group = self.create({
            'name': 'Attendee',
            'implied_ids': [(6, 0, [])],
            'category_id': self.env.ref('base.module_category_hidden').id,
        })

        return event_manager_group, organizer_group, attendee_group

class IrRule(models.Model):
    _inherit = 'ir.rule'

    @api.model
    def create_rules(self):
        # Create rule for Event Manager group
        self.create({
            'name': 'Event Manager Rule',
            'model_id': False,
            'domain_force': "[(1,'=',1)]",
            'groups': [(4, self.env.ref('your_module_name.event_manager_group').id)],
            'perm_read': True,
            'perm_write': True,
            'perm_create': True,
            'perm_unlink': True,
        })

        # Create rule for Organizer group
        self.create({
            'name': 'Organizer Rule',
            'model_id': False,
            'domain_force': "[(1,'=',1)]",
            'groups': [(4, self.env.ref('your_module_name.organizer_group').id)],
            'perm_read': True,
            'perm_write': True,
            'perm_create': True,
            'perm_unlink': True,
        })

        # Create rule for Attendee group
        self.create({
            'name': 'Attendee Rule',
            'model_id': False,
            'domain_force': "[('attendee_id','=',uid)]",
            'groups': [(4, self.env.ref('your_module_name.attendee_group').id)],
            'perm_read': True,
            'perm_write': False,
            'perm_create': False,
            'perm_unlink': False,
        })

        return True

# Call the create_groups and create_rules methods to create the groups and rules
ResGroups.create_groups()
IrRule.create_rules()





