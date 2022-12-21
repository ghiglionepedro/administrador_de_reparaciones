# -*- coding: utf-8 -*-
{
    'name': "Administrador de reparaciones",

    'summary': """
        Versión para Odoo del sistema Adro""",

    'description': """
        Versión para Odoo del sistema Adro
    """,

    'author': "Ghiglione Pedro Matias",
    'website': "www.linkedin.com/in/pedro-matias-ghiglione",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Reparaciones',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','stock','sale', 'account','repair'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'data/data.xml',
        'views/views_marca.xml',
        'views/views_modelo.xml',
        'views/views_tipo_equipo.xml',
        'views/views_menu_configuracion.xml',
        'views/views_menu_productos.xml',
        'security/ir.model.access.csv',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
