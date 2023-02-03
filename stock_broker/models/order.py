# -- coding: utf-8 
# from yahoo_fin.stock_info import *
from odoo import fields,models,api

class order(models.Model):
    _name = "orders"
    _description="model description"
    _inherits = {'listed.company': 'company_name'}

    name=fields.Char(compute="_compute_name")
    user=fields.Many2one("users",string="User Name",required=True)
    number_of_shares=fields.Integer(string="Total Shares",required=True)
    company_name=fields.Many2one("listed.company",string="Comapany Name",required=True)
    price_at_execution=fields.Float(string="Price/unit",compute="_get_stock_price",store=True)
    @api.depends("company_name")
    def _get_stock_price(self):
        for record in self:
            if record.company_name.ticker_name:
                print("....>")
                record.price_at_execution=record.company_name.current_price
            else:
                record.price_at_execution=0
        
    state=fields.Char()
    category=fields.Many2one(related="company_name.category")
    # order_type=fields.Char(string="Order type")
    total_amount=fields.Float(string="Amount",compute="_compute_total")
    portfolio_id=fields.Many2one("portfolio",string="Portfolio")
    order_type=fields.Selection(selection=[('buy','Buy'),('sell','Sell')],string="Order Type")
    @api.depends("user","order_type","total_amount")
    def _compute_name(self):
        for record in self:
            if record.user and record.total_amount and record.order_type:
                record.name=record.user.name+record.order_type+"@"+str(record.total_amount)
            else:
                record.name=record.user.name

    @api.depends("price_at_execution","number_of_shares")
    def _compute_total(self):
        for record in self:
            record.total_amount=record.price_at_execution*record.number_of_shares

    @api.model
    def create(self,vals):
        user=self.env['users'].browse(vals['user'])
        company=self.env['listed.company'].browse(vals['company_name'])
        if self.env['portfolio'].search([('name','=',user.name+company.name)]):
            print("fffffff")
        else:
            print("nnnfffff")
            self.env['portfolio'].create({'company_name':company.name, 'user_name':user.name})

        breakpoint()
        vals['portfolio_id']=self.env['portfolio'].search([('name','=',user.name+company.name)])
        return super().create(vals)
    #     user = self.env['users'].browse(vals['user'])

    #     company_name= self.env['listed.company'].browse(vals['company_name'])
    #     if vals['order_type']=='sell':           
    #         user.current_balance=user.current_balance+(vals['number_of_shares']*company_name.current_price)
    #         company_name.available_shares=company_name.available_shares+vals['number_of_shares']
    #     else:        
        
    #         user.current_balance=user.current_balance-(vals['number_of_shares']*company_name.current_price)
    #         company_name.available_shares=company_name.available_shares-vals['number_of_shares']

        

        

    def execute_buy_order(self):        
        for record in self:
            record.order_type='buy'
            record.user.current_balance=record.user.current_balance-record.total_amount
            record.company_name.available_shares=record.company_name.available_shares-record.number_of_shares 
              

    def execute_sell_order(self):        
        for record in self:
            record.order_type='sell'
            print("....>sold")
            record.user.current_balance=record.user.current_balance+record.total_amount
            record.company_name.available_shares=record.company_name.available_shares+record.number_of_shares
        
    #         