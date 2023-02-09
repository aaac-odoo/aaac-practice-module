# -- coding: utf-8 
# from yahoo_fin.stock_info import *
from odoo import fields,models,api
from odoo.exceptions import UserError, ValidationError

class order(models.Model):
    _name = "orders"
    _description="model description"
    _inherits = {'listed.company': 'company_name'}

    name=fields.Char(compute="_compute_name")
    user=fields.Many2one("users",string="User Name",required=True)
    number_of_shares=fields.Integer(string="Total Shares",required=True)
    company_name=fields.Many2one("listed.company",string="Comapany Name",required=True)
    price_at_execution=fields.Float(string="Price/unit",related="company_name.current_price",store=True)

    category=fields.Many2one(related="company_name.category")
    total_amount=fields.Float(string="Amount",compute="_compute_total",store=True)
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

    def link_portfolio(self,vals,user,company):

        print(f"oncreate {vals}")
        print(company)
        if self.env['portfolio'].search([('name','=',user.name+company.name)]):
            print("fffffff")
        else:
            print("nnnfffff")
            self.env['portfolio'].create({'company':company._origin.id, 'user':user._origin.id})
        
        portfolio=self.env['portfolio'].search([('name','=',user.name+company.name)])
        print(portfolio)
        vals['portfolio_id']=portfolio._origin.id  
        print("************")
        return portfolio

    def execute_buy_order(self,vals,user,company):
        if(vals['number_of_shares']<=company.available_shares):
            portfolio=self.link_portfolio(vals,user,company)
            portfolio.number_of_shares=portfolio.number_of_shares+vals['number_of_shares']
            portfolio.amount_invested+=(vals['number_of_shares']*(company.current_price))
            user.current_balance=user.current_balance-(vals['number_of_shares']*(company.current_price))
            company.available_shares=company.available_shares-vals['number_of_shares']
        else:        
            raise UserError(f'Only {company.available_shares} available to buy')


    def execute_sell_order(self,vals,user,company):
        portfolio=self.link_portfolio(vals,user,company)
        if(vals['number_of_shares']<=portfolio.number_of_shares):
            portfolio.number_of_shares=portfolio.number_of_shares-vals['number_of_shares']
            portfolio.amount_invested-=(vals['number_of_shares']*(company.current_price))
            user.current_balance=user.current_balance+(vals['number_of_shares']*(company.current_price))
            company.available_shares=company.available_shares+vals['number_of_shares']  
        else:        
            raise UserError(f'You have only {portfolio.number_of_shares} {company.name} shares in your portfolio')

    @api.model
    def create(self,vals):

        # print(f"oncreate {vals}")
        # user=self.env['users'].browse(vals['user'])
        # company=self.env['listed.company'].browse(vals['company_name'])
        # print(company)
        # if self.env['portfolio'].search([('name','=',user.name+company.name)]):
        #     print("fffffff")
        # else:
        #     print("nnnfffff")
        #     self.env['portfolio'].create({'company':company._origin.id, 'user':user._origin.id})
        
        # portfolio=self.env['portfolio'].search([('name','=',user.name+company.name)])
        # print(portfolio)
        # vals['portfolio_id']=portfolio._origin.id  

        user=self.env['users'].browse(vals['user'])
        company=self.env['listed.company'].browse(vals['company_name'])
        if vals['order_type']=='buy':
            print(">>>>>>>>>")
            self.execute_buy_order(vals,user,company)
        else:
            self.execute_sell_order(vals,user,company)

        # portfolio=self.link_portfolio(vals,user,company)
        # if vals['order_type']=='buy':
        #     portfolio.number_of_shares=portfolio.number_of_shares+vals['number_of_shares']
        #     portfolio.amount_invested+=(vals['number_of_shares']*(company.current_price))
        #     user.current_balance=user.current_balance-(vals['number_of_shares']*(company.current_price))
        #     company.available_shares=company.available_shares-vals['number_of_shares']
        # else:
        #     portfolio.number_of_shares=portfolio.number_of_shares-vals['number_of_shares']
        #     portfolio.amount_invested-=vals['number_of_shares']*(company.current_price)
        #     user.current_balance=user.current_balance+(vals['number_of_shares']*(company.current_price))
        #     company.available_shares=company.available_shares+vals['number_of_shares']
    

        return super().create(vals)