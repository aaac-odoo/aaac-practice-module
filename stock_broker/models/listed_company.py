# -- coding: utf-8 
from odoo import fields,models,api

class listedCompany(models.Model):
    _name = "listed.company"
    _description="model description"


    name=fields.Char(string="Comapany Name", required=True)
    available_shares=fields.Integer(required=True)
    initial_price=fields.Float(required=True)
    current_price=fields.Float(required=True)
    order_ids=fields.One2many("orders","company_name",string="Orders")