from odoo import api, fields, models


class SchoolTutors(models.Model):
    _name = "school.tutor"
    _description = "Tutor Table"

    @api.depends('name', 'surname', 'secondname')
    def _compute_fullname(self):
        for record in self:
            record.fullname = "%s %s %s" % record.surname, record.name, record.secondname

    name = fields.Char(string="Name", required=True)
    surname = fields.Char(string="Surname", required=True)
    secondname = fields.Char(string="SecondName", required=True)
    fullname = fields.Char(compute='_compute_fullname')
    specialization = fields.Char(string="Specialization")
    subject_description = fields.Text(string="Subject Description")
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], string='Gender', default='other')
    image = fields.Binary(string='Image')
