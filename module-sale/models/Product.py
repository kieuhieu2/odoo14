from odoo import models, fields, api


class Product(models.Model):
    _name = 'sale.product'
    _description = 'Sale Product'

    product_name = fields.Char(string='Product Name')
    product_des = fields.Text(string='Product Description')
    product_company = fields.Char(string='Product Company')
    product_price = fields.Float(string='Product Price')
    product_quantity = fields.Integer(string='Product quantity')
    total = fields.Float(string='Product Total', compute='_compute_total')

    @api.depends('product_price','product_quantity')
    def _compute_total(self):
        for product in self:
            product.total = product.product_price * product.product_quantity
