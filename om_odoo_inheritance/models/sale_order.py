from odoo import models, fields, api



class SaleOrder(models.Model):
    _name = 'sale.order'
    _description = 'Sale Order'
    _inherit = 'sale.order'

    confirmed_user_id = fields.Many2one(comodel_name='res.users', string='Confirmed User')

    def action_confirm(self):
        super (SaleOrder, self).action_confirm()
        print("Success.....")
        self.confirmed_user_id = self.env.user.id 
    
    