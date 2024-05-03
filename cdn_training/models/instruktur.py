from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Instruktur(models.Model):
    _name = 'instruktur'
    _description = 'Instruktur'
    _inherits = {'res.partner': 'partner_id'}

    partner_id = fields.Many2one(comodel_name='res.partner', string='Partner ID', ondelete='cascade', required=True)
    jabatan_id = fields.Many2one(comodel_name='jabatan', string='jabatan')
    keahlian_ids = fields.Many2many(comodel_name='keahlian', string='Keahlian')
    jabatan_staff = fields.Char(string='Jabatan Staff')
    jenis_jabatan = fields.Selection(string='Jenis Jabatan', related='jabatan_id.jenis_jabatan')

    def action_update_jabatan(self):
        self.jabatan_id.pejabat = self.id
        return True
    
    
class Jabatan(models.Model):
    _name = 'jabatan'
    _description = 'Jabatan'
    _rec_name = 'nama_jabatan'

    nama_jabatan = fields.Char(string='Nama Jabatan')
    jenis_jabatan = fields.Selection(string='Jenis Jabatan', selection=[('kepala_lembaga', 'Kepala Lembaga'), ('wakil_lembaga', 'Wakil Lembaga'), ('staff', 'Staff')], default="staff", required=True)
    keterangan = fields.Char(string='Keterangan')
    pejabat = fields.Many2one(comodel_name='instruktur', string='Daftar Pejabat',readonly=True)


class Keahlian(models.Model):
    _name = 'keahlian'
    _description = 'Keahlian'

    name = fields.Char(string='Nama Keahlian', required=True)
    

# @api.depends('jabatan_id')
# def _compute_jabatan_staff(self):
#     for record in self:
#         if record.jabatan_id.jenis_jabatan == 'staff':
#             record.jabatan_staff = record.jabatan_id.nama_jabatan

# @api.constrains('jabatan_id')
# def _check_kepala_wakil(self):
#     for instruktur in self:
#         kepala_wakil_count = self.env['instruktur'].search_count([
#             ('jabatan_id.jenis_jabatan', 'in', ['kepala', 'wakil_kepala']),
#             ('id', '!=', instruktur.id)
#         ])
#         if kepala_wakil_count > 0 and instruktur.jabatan_id.jenis_jabatan in ['kepala_lembaga', 'wakil_lembaga']:
#             raise ValidationError("Tidak boleh ada lebih dari satu instruktur yang menjabat %s" % instruktur.jabatan_id.jenis_jabatan)

