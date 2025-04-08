from odoo import api, fields, models, _


class StudentSubject(models.Model):
    _name = 'student.subject'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Student Subject'

    student_id = fields.Many2one('student.student', string='Student', ondelete='cascade')
    name = fields.Char(string='Subject Name', required=True)
    code = fields.Char(string="Code", required=True)
    marks = fields.Integer(string='Marks')
    lecturer = fields.Many2one('res.users', string='Lecturer')

