from odoo import models, fields, api, _
import datetime
from odoo.exceptions import ValidationError
from datetime import date
from dateutil.relativedelta import relativedelta

class CancelAppointmentWizard(models.TransientModel):
    _name = 'cancel.appointment.wizard'
    _description = 'Cancel Appointment Wizard'

    appointment_id = fields.Many2one(comodel_name='hospital.appointment', string='Appointment', domain=[('state', '=', 'draft'), ('priority', 'in', ('0','1', False))])
    reason = fields.Text(string='Reason')
    date_cancel = fields.Date(string='Cancellation Date')
    
    @api.model
    def default_get(self, fields):
        res= super(CancelAppointmentWizard, self).default_get(fields)
        res['date_cancel'] = datetime.date.today()
        if self.env.context.get('active_id'):
            res['appointment_id'] = self.env.context.get('active_id')
        return res
    
    def action_cancel(self):

        cancel_day = self.env['ir.config_parameter'].get_param('om_hospital.cancel_day')
        print("cancel_day", cancel_day)
        allowed_date = self.appointment_id.booking_date - relativedelta(days=int(cancel_day))
        if allowed_date < date.today():
            raise ValidationError(_("Sorry, cancellation is not allowed on the same day of booking !"))
        self.appointment_id.state = 'cancel'
        return {
            'type': 'ir.actions.client',
            'tag': 'reload',
        }