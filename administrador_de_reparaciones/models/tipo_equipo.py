from odoo.exceptions import ValidationError
from odoo import models, fields

class administrador_reparaciones_tipo_equipo(models.Model):
    _name = 'product.product.tipo.equipo'
    _description = 'Tipo de equipo'

    nombre = fields.Char(string='Nombre', required=True)
    marca_id = fields.Many2many ('product.product.marca', string='Marca', required=True)