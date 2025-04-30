from odoo import api, fields, models, _
from datetime import datetime
from email.policy import default


class StudentStudent(models.Model):
    _name = 'student.student'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Student Information'

    active = fields.Boolean(string='Active', default=True)
    studentid = fields.Char(string='Student ID', required=True, default='New', readonly=True)
    name = fields.Char(string='Student Name', required=True, tracking=True)
    email = fields.Char(string='Student Email', tracking=True)
    phone = fields.Char(string='Student number', tracking=True)
    mobile = fields.Char(string='Mobile Number', tracking=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender', required=True, tracking=True)
    year_id = fields.Many2one(comodel_name='year.year', string='Year', required=True, tracking=True,)
    age = fields.Integer(string='Age', compute='_compute_age', tracking=True, store=True)
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

    image = fields.Image(string='Image', max_width=1024, max_height=1024)
    image_128 = fields.Image(string='Image 128', related='image', max_width=128, max_height=128)

    cv = fields.Binary(string='CV')
    cv_file_name = fields.Char(string='CV File Name')

    marks_total = fields.Float(string='Total', compute='_compute_total', store=True)

    student_tags_ids = fields.Many2many('student.tags', string='Tags')

    student_student_ids = fields.One2many('student.subject', 'student_id', string='Subjects')

    is_mobile_invisible = fields.Boolean(compute='_compute_is_mobile_invisible')


    @api.depends('student_student_ids')
    def _compute_total(self):
        for rec in self:
            rec.marks_total = sum(student.marks for student in rec.student_student_ids)

    @api.depends('phone')
    def _compute_is_mobile_invisible(self):
        self.is_mobile_invisible =  False
        self.is_mobile_invisible = False if self.phone else True

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

    def write(self, valus):
        res = super(StudentStudent, self).write(valus)
        return res

    def _get_student_name(self):
        return f"Student Report for {self.name}"

    def action_print(self):
        return self.env.ref('aspirex_student_managment.action_student_report').report_action(self)
