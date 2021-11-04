# -*- coding: utf-8 -*-

from odoo import fields, models, api

class Documentos(models.Model):
    _inherit = "muk_dms.file"
    usuarios = fields.Many2one('sitecnet.usuarios', 'Usuario')
    cliente = fields.Many2one('sitecnet.clientes', 'Cliente')
    fequipos_cliente = fields.One2many('sitecnet.equipos', 'factura_cliente', 'Facturas Equipos')
    fequipos_interna = fields.One2many('sitecnet.equipos', 'factura_interna', 'Facturas Internas de Equipos') # configurar que solo sean usuarios administradores
    software = fields.Many2many('sitecnet.software',
                              'software_documentos_rel',
                              'documentos_id',
                              'software_id',
                              string='Licencias')
    categoria_documentos = fields.Many2one('sitecnet.categoria_documentos', 'Categoria de Documentos')

Documentos()

class categoria(models.Model):
    _name = 'sitecnet.categoria_documentos'
    _rec_name = 'name'

    name = fields.Char('Categoria')

categoria()


class resUsers(models.Model):
    _inherit = "res.Users"
    usuarios = fields.Many2one('sitecnet.usuarios', 'Usuarios')
    cliente = fields.Many2one('sitecnet.clientes', 'Cliente')
    tipo = fields.Selection([('administrador', 'Administrador'),
                               ('usuario', 'Usuario'),
                               ('tecnico', 'Tecnico'),
                               ], string='Tipo de Usuario', default='usuario')

resUsers()