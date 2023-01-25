# -- coding: utf-8 
from yahoo_fin.stock_info import *
from odoo import fields,models,api

class listedCompany(models.Model):
    _name = "listed.company"
    _description="model description"


    name=fields.Char(string="Comapany Name", required=True)
    ticker_name=fields.Char(string="Ticker Name", required=True)
    available_shares=fields.Integer(required=True)
    # initial_price=fields.Float(required=True)
    current_price=fields.Float(compute="_get_live_stock_price")
    order_ids=fields.One2many("orders","company_name",string="Orders")
    price_ids=fields.One2many('stock_prices',"company_name",string="prices")

    @api.depends("ticker_name")
    def _get_live_stock_price(self):
        for record in self:
            if record.ticker_name:
                print("....>")
                record.current_price=get_live_price(record.ticker_name)
            else:
                record.current_price=0
        