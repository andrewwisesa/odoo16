import random
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _inherit = 'mail.thread', 'mail.activity.mixin'
    _description = 'Hospital Appointment'
    _rec_name = 'ref'
    _order = 'id desc'

    name = fields.Char(string='Appointment Name')
    patient_id = fields.Many2one(comodel_name='hospital.patient', string='Pantient', ondelete='cascade', tracking="1")
    gender = fields.Selection(related='patient_id.gender', tracking="2")
    appointment_time = fields.Datetime(string='Appointment Time', default=fields.Datetime.now)
    booking_date = fields.Date(string='Booking Date', default=fields.Date.context_today, tracking="3")
    ref = fields.Char(string='Reference', help="Reference from patient record", tracking="4") 
    prescription = fields.Html(string='Prescription')
    priority = fields.Selection(string='Priority', selection=[('0', 'Normal'), ('1', 'Low'), ('2', 'High'), ('3', 'Very High'),])
    state = fields.Selection(string='Status', selection=[('draft', 'Draft'), ('in_consultation', 'In Consultation'), ('done', 'Done'), ('cancel', 'Cancel')], default='draft', required=True)
    doctor_id = fields.Many2one(comodel_name='res.users', string='Doctor', tracking="5")
    pharmacy_line_ids = fields.One2many(comodel_name='appointment.pharmacy.lines', inverse_name='appointment_id', string='Pharmacy Lines')
    hide_sales_price = fields.Boolean(string='Hide Sales Price')
    operation_id = fields.Many2one(comodel_name='hospital.operation', string='Operations')
    progress = fields.Integer(string='Progress', compute='_compute_progress')
    duration = fields.Float(string='Duration')
    company_id = fields.Many2one(comodel_name='res.company', string='Company', default=lambda self: self.env.company)
    currency_id = fields.Many2one(comodel_name='res.currency', related='company_id.currency_id')



    def unlink(self):
        for rec in self:
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
            if rec.state == 'draft':
                rec.state = 'in_consultation'

    def action_done(self):
        for rec in self:
            rec.state = 'done'
    
    def action_cancel(self):
        action = self.env.ref('cancel_appointment_wizard_action').read()[0]

    def action_draft(self):
        for rec in self:
            rec.state = 'draft'

    @api.depends('state')
    def _compute_progress(self):
        for rec in self:
            if rec.state == 'draft':
                progress = random.randrange(0, 25)
            elif rec.state == 'in_consultation':
                progress = random.randrange(25, 99)
            elif rec.state == 'done':
                progress = 100
            else:
                progress = 0
            rec.progress = progress





class AppointmentPharmacyLines(models.Model):
    _name = 'appointment.pharmacy.lines'
    _description = 'Appointment Pharmacy Lines'

    product_id = fields.Many2one(comodel_name='product.product', required=True)
    price_unit = fields.Float(related='product_id.list_price')
    qty = fields.Integer(string='Quantity', default="1")
    appointment_id = fields.Many2one(comodel_name='hospital.appointment', inverse_name='pharmacy_line_ids', string='Appointment')
    currency_id = fields.Many2one(comodel_name='res.currency', related='appointment_id.currency_id')
    price_subtotal = fields.Monetary('Subtotal', compute='_compute_price_subtotal', currency_field="currency_id")

    @api.depends('price_unit', 'qty')
    def _compute_price_subtotal(self):
        for rec in self:
            rec.price_subtotal = rec.price_unit * rec.qty

    
    
    


    
    


