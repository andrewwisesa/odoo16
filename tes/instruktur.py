from odoo import models, fields, api

class Instruktur(models.Model):
    _name = 'instruktur'
    _description = 'Instruktur'
    _inherits = {'res.partner': 'partner_id'}

    partner_id = fields.Many2one(comodel_name='res.partner', string='Partner ID', ondelete='cascade', required=True)
    keahlian_ids = fields.Many2many(comodel_name='keahlian', string='Keahlian')
    hobi_id = fields.Many2one(comodel_name='hobi', string='Hobi')
    jabatan_id = fields.Many2one(comodel_name='jabatan', string='Jabatan')
    

class Keahlian(models.Model):
    _name = 'keahlian'
    _description = 'Keahlian'

    name = fields.Char(string='Nama Keahlian', required=True)



class Hobi(models.Model):
    _name = 'hobi'
    _description = 'Hobi'
    _rec_name = 'nm_hobi'

    nm_hobi = fields.Char(string='Nama Hobi', required=True)
    keterangan = fields.Char(string='Keterangan')
    


class Jabatan(models.Model):
    _name = 'jabatan'
    _description = 'Jabatan'

    name = fields.Char(string='Nama Jabatan', required=True)
    jns_jabatan = fields.Selection(string='Jenis Jabatan', selection=[('kepala', 'Kepala'), ('wakil', 'Wakil'),('staf', 'Staf'),])
    pejabat_id = fields.Many2one(comodel_name='instruktur', string='Pejabat')
    keterangan = fields.Text('Keterangan')
    
    


    

    


