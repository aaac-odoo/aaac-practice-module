# -- coding: utf-8 
from odoo import fields,models,api

class listedCompany(models.Model):
    _name = "users"
    _description="model description"
    _order="profit desc"

    name=fields.Char(string="Name", required=True)
    initial_balance=fields.Float(string="Initial Balance", required=True)
    current_balance=fields.Float(string="Current Balance", required=True)
    # current_holdings=fields.Float(compute="_compute_holdings")
    profit=fields.Float(string="Profit (%)", compute='_compute_profit', store=True)
    order_ids=fields.One2many("orders","user",string="Orders")
    watchlist_ids=fields.Many2many("listed.company",string="Watchlist")
    portfolio_ids=fields.One2many('portfolio','user',string="Portfolios")
    @api.depends('initial_balance','current_balance')
    def _compute_profit(self):
        for record in self:
            record.profit=((record.current_balance - record.initial_balance)/record.current_balance)*100

    # @api.depends('order_ids'):
    #     for record in self:
    #         for order in record.order_ids:
    #             if