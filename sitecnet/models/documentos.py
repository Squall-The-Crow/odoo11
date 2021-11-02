# -*- coding: utf-8 -*-

from odoo import models, fields, api

class documentos(models.Model):
    _name = 'sitecnet.documentos'
    _rec_name = 'name'

    name = fields.Char('documento', required=True, )
    cliente = fields.Many2one('sitecnet.clientes', string='Cliente')  # Configurar
    #responsable
    tipo = fields.Many2one('sitecnet.categoria_documentos', string='Tipo de documento')  # Configurar
    equipos = fields.One2many('Equipo')  # Configurar,
    software = fields.One2many('Software')  # Configurar,
    #servicio
    usuario = fields.Many2one('sitecnet.usuario', string='Usuario')  # Configurar,

class categoria_documentos(models.Model):
    _name = 'sitecnet.categoria_documentos'
    _rec_name = 'name'

    name = fields.Char('Tipo de documento', required=True, )