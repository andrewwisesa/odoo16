from odoo import models, fields, api
from odoo.tools.safe_eval import safe_eval

class OdooPlayground(models.Model):
    _name = 'odoo.playground'
    _description = 'Odoo Playground'

    DEFAULT_ENV_VARIABLES = """# Available variables:
    # - self: Current Object
    # - self.env: Odoo Environment on which the action is triggered
    # - self.env.user: Return the current user (as an instance)
    # - self.is_system: Return whether the current user has group "Settings", or is in superuser mode.
    # - self.is_admin: Return whether the current user has group "Access Right", or is in superuser mode.
    # - self.is_superuser: Return whether the environment is in superuser mode.
    # - self.env.company: Return the current company (as an instance)
    # - self.env.companies: Return a recordset of the enable companies by the user
    # - self.env.lang: Return the current language code 
    # - self.env.cr: Cursor
    # - self.env.context: Context\n\n\n\n"""

    model_id = fields.Many2one(comodel_name='ir.model', string='Model')
    code = fields.Text(string='CODE', widget="ace" ,default=DEFAULT_ENV_VARIABLES)
    result = fields.Text(string='Result')
    
    def action_execute(self):
        try:
            if self.model_id:
                model = self.env[self.model_id.model]
            else:
                model = self
            self.result = safe_eval(self.code.strip(), {'self': model})
        except Exception as e:
            self.result = str(e)
    
    
