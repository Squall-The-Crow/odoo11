# -*- coding: utf-8 -*-

from odoo import fields, models, api

class documentos(models.Model):
    _inherit = "muk_dms.file"
    empresa = fields.Many2one('res.partner', 'Empresa')
    usuario = fields.Many2one('res.partner', 'Usuario')#poner filtro y dominio
    fequipos_cliente = fields.One2many('sitecnet.equipos', 'factura_cliente', 'Facturas Equipos')
    fequipos_interna = fields.One2many('sitecnet.equipos', 'factura_interna', 'Facturas Internas de Equipos') # configurar que solo sean usuarios administradores
    software = fields.Many2many('sitecnet.software',
                              'software_documentos_rel',
                              'documentos_id',
                              'software_id',
                              string='Licencias')
    categoria_documentos = fields.Many2one('sitecnet.categoria_documentos', 'Categoria de Documentos')

documentos()

class categoria(models.Model):
    _name = 'sitecnet.categoria_documentos'
    _rec_name = 'name'

    name = fields.Char('Categoria')

categoria()