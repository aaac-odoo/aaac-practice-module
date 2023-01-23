# -- coding: utf-8 
from odoo import fields,models,api
from . import order
class listedCompany(models.Model):
    _name = "users"
    _description="model description"

    name=fields.Char(string="Name", required=True)
    initial_balance=fields.Float(string="Initial Balance", required=True)
    current_balance=fields.Float(string="Current Balance", required=True)


    order_ids=fields.One2many("orders","user",string="Orders")