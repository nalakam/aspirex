from odoo import api, fields, models, _
from datetime import datetime


class StudentStudent(models.Model):
    _name = 'student.student'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Student Information'

    active = fields.Boolean(string='Active', default=True)
    studentid = fields.Char(string='Student ID', required=True, tracking=True, default='New', readonly=True)
    name = fields.Char(string='Student Name', required=True, tracking=True)
    email = fields.Char(string='Student Email', tracking=True)
    phone = fields.Char(string='Student number', tracking=True)
    mobile = fields.Char(string='Mobile Number', required=True, tracking=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender', required=True, tracking=True)
    year_id = fields.Many2one(comodel_name='year.year', string='Year', required=True, tracking=True)
    age = fields.Integer(string='Age', compute='_compute_age' ,tracking=True, store=True)
    height = fields.Float(string='Height', tracking=True)
    state = fields.Selection([('draft', 'Draft'), ('confirm', 'Confirm'), ('cancel', 'Cancelled')], string='Status',
                          tracking=True, default='draft')
    currency_id = fields.Many2one('res.currency', string='Currency')
    course_fee = fields.Monetary(string='Course Fee')
    remarks = fields.Html(string='Remarks')

    is_leave = fields.Boolean(string='Leave', default=False)
    location = fields.Selection([('colombo', 'Colombo'), ('gampaha', 'Gampaha')], string='Location')
    lecturer = fields.Many2one('res.users', string='lecturer')

    year_code = fields.Integer(related='year_id.short_code', string='Year Code', store=True)
    city_name = fields.Char(string='City Name')

    @api.onchange('location')
    def _onchange_city_name(self):
        for rec in self:
            rec.city_name = rec.location

    @api.depends('year_id')
    def _compute_age(self):
        for rec in self:
            rec.age = datetime.today().year - int(rec.year_id.name)

    def action_confirm(self):
        for rec in self:
            if rec.state == 'draft':
                rec.state = 'confirm'

    def action_cancel(self):
        for rec in self:
            if not rec.state == 'cancel':
                rec.state = 'cancel'

    @api.model_create_multi
    def create(self, value_list):
        for vals in value_list:
            vals['studentid'] = self.env['ir.sequence'].next_by_code('student.sequence') or 'New'
        res = super(StudentStudent, self).create(value_list)
        return res