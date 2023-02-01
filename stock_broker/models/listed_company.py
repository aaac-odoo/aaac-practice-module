# -- coding: utf-8 
# from yahoo_fin.stock_info import *
from odoo import fields,models,api
import random

class listedCompany(models.Model):
    _name = "listed.company"
    _description="model description"


    name=fields.Char(string="Comapany Name", required=True)
    ticker_name=fields.Char(string="Ticker Name", required=True)
    available_shares=fields.Integer(required=True)
    initial_price=fields.Integer(string="Initial Price",default=50)
    current_price=fields.Float(compute="_get_live_stock_price")
    order_ids=fields.One2many("orders","company_name",string="Orders")
    price_ids=fields.One2many('stock_prices',"company_name",string="prices")
    category=fields.Many2one("category", string="Category")
    growth=fields.Float(string="Growth %", compute='_compute_growth')
    sequence=fields.Float(default=1)
    @api.depends('initial_price','current_price')
    def _compute_growth(self):
        for record in self:
            record.growth=((record.current_price - record.initial_price)/record.current_price)*100
            record.sequence=-1*record.growth


    @api.depends("ticker_name")
    def _get_live_stock_price(self):
        for record in self:
        #     if record.ticker_name:
        #         print("....>")
        #         record.current_price=get_live_price(record.ticker_name)
        #     else:
        #         record.current_price=0
            
            x=random.random()
            record.current_price=x*100