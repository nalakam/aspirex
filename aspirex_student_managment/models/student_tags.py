from odoo import api, fields, models, _


class StudentTags(models.Model):
    _name = 'student.tags'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Student Tags'

    name = fields.Char(string='Tag Name', required=True)
    colour = fields.Integer(string='Colour')