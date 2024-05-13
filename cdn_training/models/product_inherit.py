from odoo import models, fields, api

class ProductProduct(models.Model):
    _inherit = 'product.product'
    product_training = fields.Selection(string='Jenis Produk Training', selection=[('non_training', 'Non Produk Training'), ('konsumsi', 'Konsumsi Training'), ('training_kit', 'Peralatan Training')], default='non_training')
    
