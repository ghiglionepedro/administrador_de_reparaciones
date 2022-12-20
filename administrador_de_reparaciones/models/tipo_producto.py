from odoo.exceptions import ValidationError
from odoo import models, fields

class administrador_reparaciones_tipo_producto(models.Model):
    _name = 'product.product.tipo.producto'
    _description = 'Tipo de producto de los equipos'

    nombre = fields.Char(string='Nombre', required=True)
    marca_id = fields.Many2one('product.product.marca', string='Tipo de Producto', required=True)