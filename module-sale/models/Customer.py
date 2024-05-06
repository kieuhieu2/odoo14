from odoo import fields, models


class Customer(models.Model):
    _name = 'sale.customer'
    _description = 'Customer'

    customer_name = fields.Char(string='Customer name', required=True)
    phone_number = fields.Char(string='Phone number', required=True)
    email = fields.Char(string='Email', required=True)
