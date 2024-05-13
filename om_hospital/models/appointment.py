from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _inherit = 'mail.thread', 'mail.activity.mixin'
    _description = 'Hospital Appointment'
    _rec_name = 'ref'

    patient_id = fields.Many2one(comodel_name='hospital.patient', string='Pantient')
    gender = fields.Selection(related='patient_id.gender')
    appointment_time = fields.Datetime(string='Appointment Time', default=fields.Datetime.now)
    booking_date = fields.Date(string='Booking Date', default=fields.Date.context_today)
    ref = fields.Char(string='Reference', help="Reference from patient record") 
    prescription = fields.Html(string='Prescription')
    priority = fields.Selection(string='Priority', selection=[('0', 'Normal'), ('1', 'Low'), ('2', 'High'), ('3', 'Very High'),])
    state = fields.Selection(string='Status', selection=[('draft', 'Draft'), ('in_consultation', 'In Consultation'), ('done', 'Done'), ('cancel', 'Cancel')], default='draft', required=True)
    doctor_id = fields.Many2one(comodel_name='res.users', string='Doctor', tracking=True)
    pharmacy_line_ids = fields.One2many(comodel_name='appointment.pharmacy.lines', inverse_name='appointment_id', string='Pharmacy Lines')
    hide_sales_price = fields.Boolean(string='Hide Sales Price')
        
    def unlink(self):
        if self.state != 'draft':
            raise ValidationError(_("You can delete appointment only in draft status"))
        return super(HospitalAppointment, self).unlink()

    @api.onchange('patient_id')
    def onchange_patient_id(self):
        self.ref = self.patient_id.ref

    def action_test(self):
        print("Button Clicked!!!!!!!!!")
        return{
            'effect': {
                'fadeout': 'slow',
                'message': 'Click Successfull',
                'type': 'rainbow_man',
            }
        }

    def action_in_consultation(self):
        for rec in self:
            rec.state = 'in_consultation'

    def action_done(self):
        for rec in self:
            rec.state = 'done'
    
    def action_cancel(self):
        action = self.env.ref('cancel_appointment_wizard_action').read()[0]

    def action_draft(self):
        for rec in self:
            rec.state = 'draft'





class AppointmentPharmacyLines(models.Model):
    _name = 'appointment.pharmacy.lines'
    _description = 'Appointment Pharmacy Lines'

    product_id = fields.Many2one(comodel_name='product.product', required=True)
    price_unit = fields.Float(related='product_id.list_price')
    qty = fields.Integer(string='Quantity', default="1")
    appointment_id = fields.Many2one(comodel_name='hospital.appointment', inverse_name='pharmacy_line_ids', string='Appointment')

    
    
    


    
    


