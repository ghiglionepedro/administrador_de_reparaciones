from odoo.exceptions import ValidationError
from odoo import models, fields

class administrador_reparaciones_modelo(models.Model):
    _name = 'product.product.modelo'
    _description = 'Modelos de los equipos'

    nombre = fields.Char(string='Nombre', required=True)
    marca_id = fields.Many2one('product.product.marca', string='Marca', required=True)
    tipo_equipo_id = fields.Many2one(related='product.product.marca.tipo_equipo_id', string='Tipo de equipo', readonly=True)
