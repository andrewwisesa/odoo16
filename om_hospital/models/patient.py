from odoo import models, fields, api, _
from datetime import date
from odoo.exceptions import ValidationError
from dateutil.relativedelta import relativedelta

class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _inherit = 'mail.thread', 'mail.activity.mixin'
    _description = 'Hospital patient'

    name = fields.Char(string='Name', tracking=True)
    date_of_birth = fields.Date(string='Date Of Birth')
    ref = fields.Char(string='Reference')
    age = fields.Integer(string='Age', compute='_compute_age', inverse='_inverse_compute_age', 
    search='_search_age', tracking=True)
    gender = fields.Selection(string='Gender', selection=[('male', 'Male'), ('female', 'Female'),], tracking=True, default='female')
    active = fields.Boolean(string="Active", default=True)
    appointment_id = fields.Many2one(comodel_name='hospital.appointment', string='Patient')
    image = fields.Image(string="Image")
    tag_ids = fields.Many2many(comodel_name='patient.tag', string='Tags')
    appointment_count = fields.Integer(string='Appointment Count', compute='_compute_appointment_count', store=True)
    appointment_ids = fields.One2many(comodel_name='hospital.appointment', inverse_name='patient_id', string='Appointments')
    parent = fields.Char(string='Parent')
    marital_status = fields.Selection(string='Marital Status', selection=[('married', 'Married'), ('single', 'Single'),], tracking=True)
    partner_name = fields.Char(string='Partner_name')
    is_birthday = fields.Boolean(string='Birthday ?', compute='_compute_is_birthday')
    phone = fields.Char(string='Phone')
    email = fields.Char(string='Email')
    website = fields.Char(string='Website')
    
    
    @api.depends('appointment_ids')
    def _compute_appointment_count(self):
            appointment_group = self.env['hospital.appointment'].read_group(domain=['state', '=', 'done'], fields=['patient_id'], 
            groupby=['patient_id'])

            for appointment in appointment_group:
                patient_id = appointment.get('patient_id')[0]
                patient_rec = self.browse('patient_id')
                patient_rec.appointment_count = appointment['patient_id_count']
                self -= patient_rec
            self.appointment_count = 0
            # rec.appointment_count = self.env['hospital.appointment'].search_count([('patient_id', '=', rec.id)])
    
    @api.constrains('date_of_birth')
    def _check_date_of_birth(self):
        for rec in self:
            if rec.date_of_birth and rec.date_of_birth > fields.Date.today():
                raise ValidationError(_("The entered date of birth is not acceptable !"))

    @api.ondelete(at_uninstall=False)
    def _check_appointments(self):
        for rec in self:
            if rec.appointment_ids:
                raise ValidationError(_("You cannot delete a patient with appointments"))
    
    @api.model
    def create(self, values):
        values['ref']=self.env['ir.sequence'].next_by_code('hospital.patient')
        return super(HospitalPatient, self).create(values)

    def write(self, values):
        if not self.ref and not values.get('ref'):
            values['ref'] = self.env['ir.sequence'].next_by_code('hospital.patient')
        return super(HospitalPatient, self).write(values) 

    @api.depends('date_of_birth')
    def _compute_age(self):
        for rec in self:
            today = date.today()
            if rec.date_of_birth:
                rec.age = today.year - rec.date_of_birth.year 
            else :
                rec.age = 1

    @api.depends('age')
    def _inverse_compute_age(self):
        today = date.today()
        for rec in self:
            rec.date_of_birth = today - relativedelta(years=rec.age)

    def _search_age(self, operator, value):
        date_of_birth = date.today() - relativedelta(years=value)
        start_of_year = date_of_birth.replace(day=1,month=1)
        end_of_year = date_of_birth.replace(day=31,month=12)
        return[('date_of_birth', '>=', start_of_year), ('date_of_birth', '<=', end_of_year)]

    def name_get(self):
        return [(record.id, "[%s] %s" % (record.ref, record.name)) for record in self]
    
    def action_test(self):
        print("Clicked")
        return

    def action_done(self):
        return

    @api.depends('date_of_birth')
    def _compute_is_birthday(self):
        for rec in self:
            is_birthday = False
            if rec.date_of_birth:
                today = date.today()
                if today.day == rec.date_of_birth.day and today.month == rec.date_of_birth.month:
                    is_birthday = True
            rec.is_birthday = is_birthday
    

    # def action_edit(self):
    #     return {
    #         'type': 'ir.actions.act_window',
    #         'res_model': 'hospital.appointment',
    #         'view_mode': 'form',
    #         'view_type': 'form',
    #         'res_id': self.id,
    #         'target': 'current',
    #     }
    
    
    
    
