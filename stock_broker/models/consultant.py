from odoo import fields,models,api

class Consultant(models.Model):
    _inherit="res.users"
    _description="model description"

    client_ids=fields.Many2many("users",string="Clients")
    about=fields.Char(string="About")