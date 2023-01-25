# -- coding: utf-8 
from odoo import fields,models,api
from . import order

class listedCompany(models.Model):
    _name = "stock_prices"
    _description="model description"

    company_name=fields.Many2one('listed.company',string="Comapany Name")
    year=fields.Integer(required=True, string="Year")
    price=fields.Float(required=True, string="Price")