from odoo.exceptions import ValidationError
from odoo import models, fields

class administrador_reparaciones_product(models.Model):
    _inherit = 'product.product'

    
    tipo_equipo_id = fields.One2many(related='product.product.tipo.equipo', string='Tipo de equipo')
    marca_id = fields.One2many(related='product.product.marca', string='Marca')
    modelo_id = fields.One2many(related='product.product.modelo', string='Modelo')

class administrador_reparaciones_product_template(models.Model):
    _inherit = 'product.template'

    
    tipo_equipo_id = fields.One2many(related='product.product.tipo.equipo', string='Tipo de equipo')
    marca_id = fields.One2many(related='product.product.marca', string='Marca')
    modelo_id = fields.One2many(related='product.product.modelo', string='Modelo')