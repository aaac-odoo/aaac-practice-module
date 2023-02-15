from odoo import fields,models,api

class Sip(models.Model):
    _name="sip.sip"
    _description="model description"

    user_id=fields.Many2one("users",string="User")
    category_id=fields.Many2one("category",string="Category")

    amount=fields.Integer(string="Amount/Installment")
    installment_type=fields.Selection(string='Installment type',
        selection=[('weekly','Weekly'),('monthly','Monthly'),('quarterly','Quarterly')])
    number_of_installments=fields.Integer()
    number_of_units=fields.Float()
    total_amount=fields.Integer(string="Amount invested",compute="_compute_total_amount")
    investment_value=fields.Float(string="Investment value", compute="_compute_investment_value")

    @api.depends('amount','number_of_installments')
    def _compute_total_amount(self):
        for record in self:
            record.total_amount=record.amount*record.number_of_installments


    @api.depends('number_of_installments','category_id','amount')
    def _compute_investment_value(self):
        for record in self:
            if record.category_id and record.number_of_installments and record.amount:
                record.investment_value=record.number_of_units*record.category_id.average_share_price 
            else:
                record.investment_value=0

    @api.model
    def create(self,vals):
        if vals['installment_type']=='weekly':            
            self.env['weekly.sips'].create(vals)

        if vals['installment_type']=='monthly':            
            self.env['monthly.sip'].create(vals)

        if vals['installment_type']=='quarterly':            
            self.env['quarterly.sip'].create(vals)

        return super().create(vals)
