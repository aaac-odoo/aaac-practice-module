# -- coding: utf-8 
from yahoo_fin.stock_info import *
from odoo import fields,models,api

class Category(models.Model):
    _name = "category"
    _description="model description"

    name=fields.Char(string="Category Name", required=True)

    company_ids=fields.One2many("listed.company","category", string="companies")
    average_growth=fields.Float(string="Average growth", compute="_compute_growth")
    @api.depends('company_ids')
    def _compute_growth(self):
        for record in self:
            if record.company_ids:
                sum=0
                for company in record.company_ids:
                    sum=sum+company.growth
                print(sum)
                record.average_growth=sum/len(record.company_ids)
            else:
                record.average_growth=0
    order_ids=fields.One2many("orders","category",string="orders")
    order_count=fields.Integer(compute="_compute_order_count")
    @api.depends("order_count")
    def _compute_order_count(self):
        for record in self:
            record.order_count=len(record.order_ids)