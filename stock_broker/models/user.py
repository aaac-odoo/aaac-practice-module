# -- coding: utf-8 
from odoo import fields,models,api
from . import order
class listedCompany(models.Model):
    _name = "users"
    _description="model description"
    _order="growth desc"

    name=fields.Char(string="Name", required=True)
    initial_balance=fields.Float(string="Initial Balance", required=True)
    current_balance=fields.Float(string="Current Balance", required=True)
    growth=fields.Float(string="Growth %", compute='_compute_growth', store=True)
    @api.depends('initial_balance','current_balance')
    def _compute_growth(self):
        for record in self:
            record.growth=((record.current_balance - record.initial_balance)/record.current_balance)*100

    order_ids=fields.One2many("orders","user",string="Orders")