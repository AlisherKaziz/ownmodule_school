from odoo import api, fields, models


class SchoolTutors(models.Model):
    _name = "school.tutor"
    _description = "Tutor Table"

    @api.depends('name', 'surname', 'fullname')
    def _compute_fullname(self):
        self.fullname = "{} {}".format(self.name, self.surname)
        pass

    name = fields.Char(string="Name", required="True")
    surname = fields.Char(string="Surname", required="True")
    fullname = fields.Char(string="Fullname", compute="_compute_fullname")
    subject_description = fields.Text(string="Subject Description")
    gender = fields.Selection([
        ('1', 'Male'),
        ('2', 'Female'),
        ('3', 'Other')
    ], string='Gender', default='3')
    image = fields.Binary(string='Image')
