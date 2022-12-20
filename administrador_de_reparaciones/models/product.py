from odoo.exceptions import ValidationError
from odoo import models, fields

class administrador_reparaciones_product(models.Model):
    _inherit = 'product.product'

    
    tipo_equipo_id = fields.Many2one('product.product.tipo.equipo', string='Equipo', required=True)
    marca_id = fields.Many2one('product.product.marca', string='Tipo de Producto', required=True)
    modelo_id = fields.Many2one('product.product.modelo', string='Modelo', required=True)