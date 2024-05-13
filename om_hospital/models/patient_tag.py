from odoo import models, fields, api, _


class PatientTag(models.Model):
    _name = 'patient.tag'
    _inherit = 'mail.thread', 'mail.activity.mixin'
    _description = 'Patient Tag'

    name = fields.Char(string='Name', required=True)
    active = fields.Boolean(string='Active', default=True, copy=False)
    color = fields.Integer(string='Color')
    color_2 = fields.Char(string='Color')
    sequence = fields.Integer(string='Sequence')
    
    @api.returns('self', lambda value: value.id)
    def copy(self, default=None):
        if default is None:
            default = {}

        if not default.get('name'):
            default['name'] = _("%s (copy)", self.name)
        
        default['sequence'] = 10
        return super(PatientTag, self).copy(default)
    
    _sql_constraints = [
        ('check_sequence', 'check(sequence > 0)', 'Sequence Must be non zero positive number.')
    ]

    
    
    
