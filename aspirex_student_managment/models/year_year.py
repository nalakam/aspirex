from odoo import api, fields, models, _


class YearYear(models.Model):
    _name = 'year.year'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Year'
    _order = 'priority desc'

    priority = fields.Selection([
        ('0', 'Normal'),
        ('1', 'Low'),
        ('2', 'High'),
        ('3', 'Very High')], string='Priority')
    name = fields.Char(string='Year Name', required=True, help='Name of the Year')
    short_code = fields.Integer(string='Year Code')