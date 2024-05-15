from odoo import models, fields, api



class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    _name = 'res.config.settings'
    _description = 'Res Config Settings'

    cancel_days = fields.Integer(string='Cancel Days', config_parameter='om_hospital.cancel_day')
    
