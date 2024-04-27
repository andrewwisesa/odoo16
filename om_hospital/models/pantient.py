from odoo import api, fields, models



class HospitalPantient(models.Model):
    _name = 'hospital.pantient'
    _description = 'Hospital Pantient'

    name = fields.Char(string='Name')
    age = fields.Integer(string='Age')
    gender = fields.Selection(string='Gender', selection=[('male', 'Male'), ('female', 'Female'),])
    
    
    
    
    
