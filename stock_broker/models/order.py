# -- coding: utf-8 
from odoo import fields,models,api

class order(models.Model):
    _name = "orders"
    _description="model description"

    user=fields.Many2one("users",string="User Name",required=True)
    number_of_shares=fields.Integer(string="Total Shares",required=True)
    company_name=fields.Many2one("listed.company",string="Comapany Name",required=True)
    price_at_execution=fields.Float(string="Price/unit",required=True,compute="_get_stock_price")
    @api.depends("company_name")
    def _get_stock_price(self):
        for record in self:
            record.price_at_execution=record.company_name.current_price

    # order_type=fields.Selection(
    #     string="Order Type",
    #     selection=[('buy', 'Buy'), ('sell', 'Sell')])

    order_type=fields.Char(required=True)
    total_amount=fields.Float(string="Amount")
    def execute_buy_order(self):        
        for record in self:
            record.total_amount=record.price_at_execution*record.number_of_shares
            record.user.current_balance=record.user.current_balance-record.total_amount
            record.company_name.available_shares=record.company_name.available_shares-record.number_of_shares 
            print("==>>>>")  



    # total_amount=fields.Float(string="Amount",compute="_compute_total")
    # @api.depends("price_at_execution","number_of_shares","order_type")
    # def _compute_total(self):
    #     for record in self:
    #         record.total_amount=record.price_at_execution*record.number_of_shares
    #         if(record.order_type=='buy'):
    #             record.user.current_balance=record.user.current_balance-record.total_amount
    #             record.company_name.available_shares=record.company_name.available_shares-record.number_of_shares 
    #             print("==>>>>")  
    #         else:
    #             record.user.current_balance=record.user.current_balance+record.total_amount
    #             record.company_name.available_shares=record.company_name.available_shares+record.number_of_shares