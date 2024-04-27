from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = "res.partner"

    propinsi_id     = fields.Many2one(comodel_name="ref.propinsi",  string="Propinsi")
    kota_id         = fields.Many2one(comodel_name="ref.kota",  string="Kota")
    kecamatan_id    = fields.Many2one(comodel_name="ref.kecamatan",  string="Kecamatan")
    desa_id         = fields.Many2one(comodel_name="ref.desa",  string="Desa/Kelurahan")
    jenis_kelamin   = fields.Selection(selection=[('laki-laki', 'Laki-Laki'), ('perempuan', 'Perempuan')], string="Jenis Kelamin")

    