from odoo.exceptions import ValidationError
from odoo import models, fields

class administrador_reparaciones_modelo(models.Model):
    _name = 'product.product.modelo'
    _description = 'Modelos de los equipos'

    nombre = fields.Char(string='Nombre', required=True)
    marca_id = fields.Many2many('product.product.marca', string='Marca', readonly=True)
    tipo_equipo = fields.Many2many('product.product.tipo.equipo', string='Marca', related="marca_id.tipo_equipo_id")
