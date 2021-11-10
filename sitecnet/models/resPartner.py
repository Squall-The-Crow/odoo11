# -*- coding: utf-8 -*-

from odoo import models, fields, api

class resPartner(models.Model):
    _inherit = "res.partner"
    director = fields.Many2one('res.partner', string='Director', ondelete='cascade', domain=[('is_company', '=', True)])
    contacto = fields.Many2one('res.partner', string='Contacto principal', ondelete='cascade', domain=[('is_company', '=', True)])
    servicios = fields.One2many('sitecnet.servicios', 'empresa', string='Servicios contratados', copy=True, auto_join=True, ondelete='cascade', domain=[('is_company', '=', True)])
    rutinas = fields.One2many('sitecnet.rutinas', 'empresa', string='Rutinas y Procesos', ondelete='cascade', domain=[('is_company', '=', True)])
    rutinas_usuario = fields.Many2many('sitecnet.rutinas',
                              'rutinas_usuarios_rel',
                              'usuarios_id',
                              'rutinas_id',
                              string='Rutinas del usuario', ondelete='cascade', domain=[('is_company', '=', False)])
    equipos = fields.One2many('sitecnet.equipos', 'empresa', string='Equipos', copy=True, auto_join=True, ondelete='cascade', domain=[('is_company', '=', True)])
    documentos = fields.One2many('muk_dms.file', 'empresa', 'Documentos', ondelete='cascade', domain=[('is_company', '=', True)])
    software = fields.One2many('sitecnet.software', 'empresa', string='Software', copy=True, auto_join=True, ondelete='cascade', domain=[('is_company', '=', True)])
    accesos = fields.One2many('sitecnet.cuentas', 'empresa', string='Accesos', copy=True, auto_join=True, ondelete='cascade', domain=[('is_company', '=', True)])
    equipos_usuario = fields.One2many('sitecnet.equipos', 'usuario', string='Equipos del Usuario', copy=True, auto_join=True, ondelete='cascade', domain=[('is_company', '=', False)])
    documentos_usuario = fields.One2many('muk_dms.file', 'usuario', 'Documentos de Usuario', ondelete='cascade', domain=[('is_company', '=', False)])
    software_usuario = fields.Many2many('sitecnet.software',
                                'software_usuarios_rel',
                                'usuario_id',
                                'software_id',
                                'Software', ondelete='cascade', domain=[('is_company', '=', False)])
    accesos_usuario = fields.One2many('sitecnet.cuentas', 'usuario', string='Accesos de Usuario', copy=True, auto_join=True, ondelete='cascade', domain=[('is_company', '=', False)])
