from odoo.exceptions import ValidationError
from odoo import models, fields

class Partner(models.Model):
    _inherit = 'res.partner'

    dni = fields.Char(string='DNI')