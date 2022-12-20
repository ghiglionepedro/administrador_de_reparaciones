from odoo.exceptions import ValidationError
from odoo import models, fields

class MiModelo(models.Model):
    _name = 'product.product.marca'
    _description = 'Marca de los equipos'

    nombre = fields.Char(string='Nombre', required=True)
    tipo_producto_id = fields.Many2one('product.product.tipo.producto', string='Tipo de Producto', required=True)