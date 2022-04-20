from odoo import fields, models


class SchoolTutors(models.Model):
    _name = "school.tutor"
    _description = "Tutor Table"

    name = fields.Char(string="Name", required=True)
    surname = fields.Char(string="Surname", required=True)
    secondname = fields.Char(string="SecondName", required=True)
    age = fields.Integer(string="Age")
    specialization = fields.Char(string="Specialization")
    subject_description = fields.Text(string="Subject Description")
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], string='Gender', default='other')
    image = fields.Binary(string='Image')


class SchoolTutorFullName(SchoolTutors.name, SchoolTutors.surname, SchoolTutors.secondname):
    _name = "school.tutor.fullname"
    _columns = {

        'name': SchoolTutors.name,
        'surname': SchoolTutors.surname,
        'secondname': SchoolTutors.secondname

    }
