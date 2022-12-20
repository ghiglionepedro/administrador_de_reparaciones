from odoo.exceptions import ValidationError
from odoo import models, fields

class administrador_reparaciones_product(models.Model):
    _inherit = 'product.product'

    
    product_id = fields.Many2one('product.product.tipo.producto', string='Equipo', required=True)
    tipo_producto_id = fields.Many2one('product.product.tipo.equipo', string='Tipo de equipo', required=True)