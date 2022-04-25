from odoo import api, fields, models


class SchoolTutors(models.Model):
    _name = "school.tutor"
    _description = "Tutor Table"

    @api.depends('name', 'surname')
    def compute_fullname(self):
        self.fullname = "{} {}".format(self.name, self.surname)

    name = fields.Char(string="Name", required="True")
    surname = fields.Char(string="Surname", required="True")
    fullname = fields.Char(strring="Fullname", compute="compute_fullname")
    subject_description = fields.Text(string="Subject Description")
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], string='Gender', default='other')
    image = fields.Binary(string='Image')
