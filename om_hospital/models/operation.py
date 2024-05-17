from odoo import models, fields, api, _



class HospitalOperation(models.Model):
    _name = 'hospital.operation'
    _description = 'Hospital Operation'
    _rec_name = 'operation_name'
    _log_access = False
    _order = 'sequence,id'

    doctor_id = fields.Many2one(comodel_name='res.users', string='Doctor')
    operation_name = fields.Char(string='Name')
    reference_record = fields.Selection([
        ('hospital.patient', 'Patient'),
        ('hospital.appointment', 'Appointment')
    ], string='Record')
    sequence = fields.Integer(string='Sequence', default=10)
    
    
    @api.model
    def name_create(self, name):
        return self.create({"operation_name": name}).name_get()[0]
    
    
