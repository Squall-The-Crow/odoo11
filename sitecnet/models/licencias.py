# -*- coding: utf-8 -*-

from odoo import models, fields, api

class software(models.Model):
    _name = 'sitecnet.software'
    _rec_name = 'name'

    name = fields.Char('Software')
    licencia = fields.Char('Numero de Licencia')
    user = fields.Char('Nombre de usuario')
    passw = fields.Char('Password')
    fecha_compra = fields.Date('Fecha de Compra', required=True, )
    vigencia = fields.Date('Vigencia', required=True, )
    empresa = fields.Many2one('res.company', string='Empresa')
    usuarios = fields.Many2many('res.partner',
                                'software_usuarios_rel',
                                'software_id',
                                'usuario_id',
                                'Usuarios asignados')
    documentos = fields.Many2many('muk_dms.file',
                              'software_documentos_rel',
                              'software_id',
                              'documentos_id',
                              string='Documentos')
    notas = fields.Text('Notas')
    categoria = fields.Many2one('sitecnet.categoria_software','Categoria')
    equipos = fields.Many2many('sitecnet.equipos',
                              'software_equipos_rel',
                              'software_id',
                              'equipos_id',
                              string='Equipo')

class categoria_software(models.Model):
    _name = 'sitecnet.categoria_software'
    _rec_name = 'name'

    name = fields.Char('Categoria')