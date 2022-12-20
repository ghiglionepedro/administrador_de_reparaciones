from odoo.exceptions import ValidationError
from odoo import models, fields

class tipo_producto(models.Model):
    _name = 'product.product.tipo.producto'
    _description = 'Tipo de producto de los equipos'

    nombre = fields.Char(string='Nombre', required=True)
    product_id = fields.Many2one('product.product', string='Equipo', required=True)