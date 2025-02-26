from odoo import models, fields, api, _


class SaleOrder(models.Model):
    _inherit = 'product.template'

    model = fields.Char(string="Model")
    b_d_detail = fields.Char(string="B/D Detail")
    b_d_date = fields.Date(string="B/D Date")
    status = fields.Selection([
        ('waiting_inspenction', 'Waiting Inspection'),
        ('waiting_part', 'Waiting Part'),
        ('unnder_progress', 'Under Progress'),
    ], string="Status", tracking=True)
    rfu_plan = fields.Char(string="Plan RFU")
    category = fields.Text(string="Category")
    part_description = fields.Text(string="Part Description")
    no_mrd = fields.Char(string="No. MRD")
    eta = fields.Char(string="ETA")
    ata = fields.Char(string="ATA")


    
