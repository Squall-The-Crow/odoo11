# -*- coding: utf-8 -*-
{
    'name': "sitecnet",

    'summary': """
        Modulo de Sistemas""",

    'description': """
        Modulos para Inventario
        Seguimiento de incidentes
        Base de ayuda y servicios
    """,

    'author': "Sitecnet",
    'website': "http://www.sitecnet.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Production',
    'version': '2.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'contacts', 'decimal_precision', 'web_google_maps', 'muk_dms_file', 'website_support'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',        
        'views/configuracion.xml',
        'views/licencias.xml',
        'views/servicios.xml',
        'views/equipos.xml',
        'views/rutinas.xml',
        'views/menu.xml',
        #'views/herencia.xml', Partners, Usuarios, documentos y tickets
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
