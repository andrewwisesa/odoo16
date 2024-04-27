from odoo import models, fields, api



class RefPropinsi(models.Model):
    _name = 'ref.propinsi'
    _description = 'Ref Propinsi'

    name = fields.Char(string='Nama Propinsi',required=True)
    kode = fields.Char(string='Kode Propinsi')
    singkat = fields.Char(string='Singkatan')
    keterangan = fields.Text('Keterangan')
    kota_ids = fields.One2many(comodel_name='ref.kota', inverse_name='propinsi_id', string='Daftar Kota')
    
class RefKota(models.Model):
    _name = 'ref.kota'
    _description = 'Ref Kota'

    name = fields.Char(string='Nama Kota',required=True)
    kode = fields.Char(string='Kode Kota')
    propinsi_id = fields.Many2one(comodel_name='ref.propinsi', string='Nama Propinsi')
    singkat = fields.Char(string='Singkatan')
    keterangan = fields.Datetime('Keterangan')
    kecamatan_ids = fields.One2many(comodel_name='ref.kecamatan', inverse_name='kota_id', string='Daftar Kecamatan')
    
class RefKecamatan(models.Model):
    _name = 'ref.kecamatan'
    _description = 'Ref Kecamatan'

    name = fields.Char(string='Nama Kecamatan',required=True)
    kode = fields.Char(string='Kode Kecamatan')
    kota_id = fields.Many2one(comodel_name='ref.kota', string='Nama Kota')
    keterangan = fields.Datetime(string='Keterangan')
    desa_ids = fields.One2many(comodel_name='ref.desa', inverse_name='kecamatan_id', string='Daftar Desa')
    

class RefDesa(models.Model):
    _name = 'ref.desa'
    _description = 'Ref Desa'

    name = fields.Char(string='Nama Desa', required=True)
    kode = fields.Char(string='Kode Desa')
    kota = fields.Char(string='Kode Desa')
    kecamatan_id = fields.Many2one(comodel_name='ref.kecamatan', string='Nama Kecamatan')
    keterangan = fields.Datetime(string='Keterangan')
    
    
    

    

    
    
    
    

    
    
    
