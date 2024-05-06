from odoo import models, fields


class Invoice(models.Model):
    _name = 'sale.invoice'
    _description = 'Sale Invoice'

    invoice_code = fields.Char(string='Number invoice')
    creation_date = fields.Datetime(string='Creation Date')
    customer_name = fields.Many2one('res.partner', string='Customer name')
    sale_person_name = fields.Many2one('res.partner', string='Sale person name')
    product_name = fields.Many2one('res.partner', string='Product name')
    total = fields.Many2one('res.partner', string='Total')


