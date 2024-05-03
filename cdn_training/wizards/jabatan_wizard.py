from odoo import models, fields, api

class JabatanWizard(models.TransientModel):
    _name = 'jabatan.wizard'
    _description = 'Jabatan wizard'

    jabatan_id = fields.Many2one(comodel_name='jabatan', string='Jabatan')
    instruktur_id = fields.Many2one(comodel_name='instruktur', string='Instruktur')
    instruktur_name = fields.Char(string='Pemangku Jabatan', related='jabatan_id.pejabat.name')
    # pejabat_id = fields.Many2one(comodel_name='instruktur', string='Pejabat')

    def simpan(self):
        # related_records = self.env['instruktur'].search([('jabatan_id','=',self.jabatan_id.id)])
        # for record in related_records:
        #     record.jabatan_id = 0

        # self.jabatan_id.pejabat = self.instruktur_id
        # self.instruktur_id.jabatan_id = self.jabatan_id.id

    # def update_jabatan(self):
        self.instruktur_id.write({'jabatan_id': self.jabatan_id.id})
        self.jabatan_id.write({'instruktur_id': self.instruktur_id.id})

        
        return {'type': 'ir.actions.act_window_close'}


    
    
    
