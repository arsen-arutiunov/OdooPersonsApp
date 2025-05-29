from odoo import models, fields, api
from datetime import date


class Person(models.Model):
    _name = 'persons.person'
    _description = 'Person'

    first_name = fields.Char(string='First Name', required=True)
    last_name = fields.Char(string='Last Name', required=True)
    full_name = fields.Char(string='Full Name',
                            compute='_compute_full_name',
                            store=True)
    birthday = fields.Date(string='Birthday')
    age = fields.Integer(string='Age', compute='_compute_age', store=True)
    sex = fields.Selection([
        ('male', 'Male'), ('female', 'Female'), ('non_binary', 'Non-binary')
    ], string='Sex')
    company_id = fields.Many2one('res.company',
                                 string='Company',
                                 required=True,
                                 default=lambda self: self.env.company)

    @api.depends('first_name', 'last_name')
    def _compute_full_name(self):
        for rec in self:
            rec.full_name = (rec.first_name or '') + ' ' + (rec.last_name or '')

    @api.depends('birthday')
    def _compute_age(self):
        today = date.today()
        for rec in self:
            if rec.birthday:
                born = rec.birthday
                rec.age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
            else:
                rec.age = 0
