from odoo import models, fields, api, _


class StudentStudent(models.Model):
    _name = 'student.student'
    _description = 'Student Information'

    name = fields.Char(string='Student Name', required=True)
    email = fields.Char(string='Student Email')
    phone = fields.Char(string='Student number')
    mobile = fields.Char(string='Mobile Number', required=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender', required=True)
    year_id = fields.Many2one(comodel_name='year.year', string='Year', required=True, tracking=True)
    age = fields.Integer(string='Age')
    height = fields.Float(string='Height')