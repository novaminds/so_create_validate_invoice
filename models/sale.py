from odoo import models, fields, api, exceptions
class sale_order(models.Model):
    _inherit = 'sale.order'

    @api.multi
    def action_confirm(self):
        res = super(sale_order, self).action_confirm()
        if res:

            self.action_invoice_create()
            for invoice in self.invoice_ids:
                invoice.action_invoice_open()
        return res

