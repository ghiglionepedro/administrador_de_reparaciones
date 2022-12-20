from odoo.exceptions import ValidationError
from odoo import models, fields

class administrador_reparaciones_partner(models.Model):
    _inherit = 'res.partner'

    dni = fields.Char(string='DNI')