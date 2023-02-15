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

    current_portfolio_value=fields.Float(compute="_compute_portfolio_value")
    # consultant_ids=fields.Many2many("res.users",string="Consultants")
    sip_ids=fields.One2many("sip.sip",'user_id',string="SIPs")
    @api.depends('initial_balance','current_balance')
    def _compute_profit(self):
        for record in self:
            record.profit=((record.current_balance - record.initial_balance)/record.current_balance)*100

    @api.depends('portfolio_ids')
    def _compute_portfolio_value(self):
        for record in self:
            record.current_portfolio_value=sum(record.portfolio_ids.mapped('current_value'))

    # @api.depends('order_ids'):
    #     for record in self:
    #         for order in record.order_ids:
    #             if