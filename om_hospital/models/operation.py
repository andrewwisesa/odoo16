from odoo import models, fields, api, _



class HospitalOperation(models.Model):
    _name = 'hospital.operation'
    _description = 'Hospital Operation'
    _log_access = False

    doctor_id = fields.Many2one(comodel_name='res.users', string='Doctor')
    operation_name = fields.Char(string='Name')
    
    @api.model
    def name_create(self, name):
        return self.create({"operation_name": name}).name_get()[0]
    
    
