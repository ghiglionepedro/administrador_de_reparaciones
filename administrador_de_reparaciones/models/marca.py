from odoo.exceptions import ValidationError
from odoo import models, fields

class administrador_reparaciones_marca(models.Model):
    _name = 'product.product.marca'
    _description = 'Marca de los equipos'

    nombre = fields.Char(string='Nombre', required=True)
    modelo_id = fields.Many2one('product.product.modelo', string='Modelo', required=True)