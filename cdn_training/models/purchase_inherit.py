from odoo import models, fields, api

class Purchaseorder(models.Model):
    _inherit = 'purchase.order'
    product_training = fields.Selection(string='Jenis Produk Training', selection=[('non_training', 'Non Produk Training'), ('konsumsi', 'Konsumsi Training'), ('training_kit', 'Peralatan Training')], default='non_training')
    
