from odoo import fields, models


class SaleTeam(models.Model):
    _name = 'sale.team'
    _description = 'Sale Team'

    sale_person_name = fields.Char(string='Sale Person Name')
