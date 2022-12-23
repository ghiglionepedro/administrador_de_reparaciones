from odoo.exceptions import ValidationError
from odoo import models, fields

class administrador_reparaciones_modelo(models.Model):
    _name = 'product.product.modelo'
    _description = 'Modelos de los equipos'

    nombre = fields.Char(string='Nombre', required=True)
    tipo_equipo_id = fields.One2many(related='marca_id.tipo_equipo_id', string='Tipo de equipo', readonly=True)
