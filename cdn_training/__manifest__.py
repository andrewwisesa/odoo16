# -*- coding: utf-8 -*-
{
    'name': "Training_Course",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Cendana2000",
    'website': "https://www.cendana2000.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '16.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','mail','product','purchase','l10n_id_efaktur'],
    # always loaded
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'data/sequence_data.xml',
        'views/menu_training.xml',
        'views/training_course.xml',
        'views/instruktur.xml',
        'views/training_session.xml',
        'views/propinsi.xml',
        'views/kota.xml',
        'views/kecamatan.xml',
        'views/desa.xml',
        'views/peserta.xml',
        'views/jabatan.xml',
        'views/product_inherit.xml',
        'views/purchase_inherit.xml',
        'views/res_partner.xml',
        'wizards/training_wizard.xml',
        'wizards/jabatan_wizard.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application':True,
}
