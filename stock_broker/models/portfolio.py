from odoo import fields,models,api

class portfolio(models.Model):
    _name = "portfolio"
    _description="model description"

    name=fields.Char(compute="_compute_name",store=True)
    company_name=fields.Char()
    user_name=fields.Char()
    order_ids=fields.One2many("orders","portfolio_id")


    @api.depends('company_name','user_name')
    def _compute_name(self):
        for record in self:
            if record.company_name and record.company_name:
                record.name=record.user_name+record.company_name
            else:
                record.name=""


    # @api.model
    # def create(self,vals):
    #     order=self.env['orders'].browse(vals['order_ids'][0])
    #     company_name=order.company_name
    #     user_name=order.user_name
    #     print("------------------->>>")
    #     return super().create(vals)