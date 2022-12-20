from odoo.exceptions import ValidationError
from odoo import models, fields

class administrador_reparaciones_tipo_equipo(models.Model):
    _name = 'product.product.tipo.equipo'
    _description = 'Tipo de producto de los equipos'

    nombre = fields.Char(string='Nombre', required=True)