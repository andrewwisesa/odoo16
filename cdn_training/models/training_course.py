from odoo import models,fields,api
from datetime import timedelta



class TrainingCourse(models.Model):
    _name = 'training.course'
    _description = 'training.course'

    nama = fields.Char(string='nama kursus', required=True)
    keterangan = fields.Text(string='keterangan')
    user_id = fields.Many2one(comodel_name='res.users', string='Penanggung Jawab')
    session_line = fields.One2many(comodel_name='training.session', inverse_name='course_id', string='Sesi Training')
    
    
    
    _sql_constraints = [
        ('name_course_unique', 'UNIQUE(nama)', 'Nama kursus sudah ada!'),
    ]


    class TrainingSession(models.Model):
        _name = 'training.session'
        _description = 'Training Session'
        _inherit = ['mail.thread', 'mail.activity.mixin']
    
        name = fields.Char(string='Sesi Training', required=True)
        course_id = fields.Many2one(comodel_name='training.course', string='ID Kursus', required=True)
        start_date = fields.Date(string='Tanggal Mulai', required=True)
        duration = fields.Float(string='Durasi', required=True)
        seats = fields.Integer(string='Max Peserta', required=True, default=1)
        instruktur_id = fields.Many2one(comodel_name='instruktur', string='Nama Instruktur')
        alamat = fields.Char(string='Alamat',related='instruktur_id.street')
        no_hp = fields.Char(string='No HP',related='instruktur_id.mobile')
        email = fields.Char(string='Email',related='instruktur_id.email')
        jenis_kel = fields.Selection(related='instruktur_id.jenis_kelamin')
        peserta_ids = fields.Many2many(comodel_name='peserta', string='Nama Peserta')
        jml_peserta = fields.Integer(compute='_compute_jml_peserta', string='Jumlah Peserta')
        state = fields.Selection(string='Status', selection=[('draft', 'Draft'), ('progress', 'Sedang Berlangsung'), ('done', 'Selesai'),],default='draft')
        end_date = fields.Char(compute='_compute_end_date', string='end_date')
        product_ids = fields.Many2many(comodel_name='product.product', string='Peralatan/Konsumsi', domain=[('product_training', '!=', 'non_training')])
        
        @api.depends('')
        def _compute_end_date(self):
            pass
        
        name = fields.Char(string='Pokok Bahasan', required=True, tracking=True)
        course_id = fields.Many2one(comodel_name='training.course', string='Kursus', ondelete='cascade', tracking=True)
        start_date = fields.Date(string='Tanggal', tracking=True)
        duration = fields.Float(string='Durasi', tracking=True)
        seat = fields.Integer(string='Peserta', tracking=True)

        
        
        @api.depends('peserta_ids')
        def _compute_jml_peserta(self):
            for rec in self:
                rec.jml_peserta = len(rec.peserta_ids)

        def action_confirm(self):
            self.state = 'progress'

        def action_done(self):
            self.state = 'done'
        
        def action_draft(self):
            self.state = 'draft'


        @api.depends('start_date', 'duration')
        def _compute_end_date(self):
            for record in self:
                if record.start_date and record.duration:
                    start_date = fields.Date.from_string(record.start_date)
                    end_date = start_date + timedelta(days=record.duration)
                    record.end_date = fields.Date.to_string(end_date)
                else:
                    record.end_date = False
        
        
        
        



        
        
    
   
