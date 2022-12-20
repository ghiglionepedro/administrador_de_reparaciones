from odoo.exceptions import ValidationError
from odoo import models, fields

class MiModelo(models.Model):
    _inherit = 'product.product'