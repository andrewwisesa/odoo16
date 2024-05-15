from odoo import models, fields, api



class ResGroups(models.Model):
    _inherit = 'res.groups'

    def get_application_groups(self, domain):
        group_id = self.env.ref('project.group_project_task_dependencies').import ipdb; ipdb.set_trace()  # noqa
        

