from odoo import fields,models,api

class portfolio(models.Model):
    _name = "portfolio"
    _description="model description"

    name=fields.Char(compute="_compute_name",store=True)
    company=fields.Many2one('listed.company',string="Comapany")
    user=fields.Many2one('users',string="User")
    order_ids=fields.One2many("orders","portfolio_id")
    amount_invested=fields.Float()
    # current_value=fields.Float(compute="_compute_current_value")
    number_of_shares=fields.Integer()


    @api.depends('company','user')
    def _compute_name(self):
        for record in self:
            if record.company.name and record.user.name:
                record.name=record.user.name+record.company.name
            else:
                record.name=""

    # @api.depends('company_name','number_of_shares')
    # def _compute_current_value(self):
    #     for record in self:
    #         record.current_value=record.company_name.current_price*record.number_of_shares

    # @api.model
    # def create(self,vals):
    #     order=self.env['orders'].browse(vals['order_ids'][0])
    #     company_name=order.company_name
    #     user_name=order.user_name
    #     print("------------------->>>")
    #     return super().create(vals)