from odoo import api, fields, models, _


class Partner(models.Model):
    _inherit = 'res.partner'

    fax_no = fields.Char(string='Fax No')
