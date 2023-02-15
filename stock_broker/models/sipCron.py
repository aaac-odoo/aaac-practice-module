from odoo import models,fields
class DemoClass(models.Model):
   _name = 'sip.cron'
   _description="model description"
   
   # student_name = fields.Char(string='Name of the student', required=True)
   def cron_demo_method(self):

      sip_ids=self.env['sip.sip'].search([('installment_type','=','weekly')])

      for sip in sip_ids:
         print(sip.user_id.name)
         sip.user_id.current_balance-=sip.amount
         sip.number_of_installments+=1
         sip.number_of_units+=sip.amount/sip.category_id.average_share_price
         
         print("Inside the function--------------->") 