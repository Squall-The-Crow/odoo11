# -*- coding: utf-8 -*-

from odoo import models, fields, api

class resPartner(models.Model):
    _inherit = "res.partner"
    director = fields.Many2one('res.partner', string='Director', select=True, domain=[('is_company', '=', True)])# if company is true
    contacto = fields.Many2one('res.partner', string='Contacto principal', select=True)# if company is true
    servicios = fields.One2many('sitecnet.servicios', 'empresa', string='Servicios contratados', copy=True)# if company is true
    rutinas = fields.One2many('sitecnet.rutinas', 'empresa', string='Rutinas y Procesos')# if company is true
    rutinas_usuario = fields.Many2many('sitecnet.rutinas',
                              'rutinas_usuarios_rel',
                              'usuarios_id',
                              'rutinas_id',
                              string='Rutinas del usuario')
    equipos = fields.One2many('sitecnet.equipos', 'empresa', string='Equipos', copy=True, auto_join=True)
    documentos = fields.One2many('muk_dms.file', 'empresa', 'Documentos')
    software = fields.One2many('sitecnet.software', 'empresa', string='Software', copy=True, auto_join=True)
    accesos = fields.One2many('sitecnet.cuentas', 'empresa', string='Accesos', copy=True, auto_join=True)
    equipos_usuario = fields.One2many('sitecnet.equipos', 'usuario', string='Equipos', copy=True, auto_join=True)
    documentos_usuario = fields.One2many('muk_dms.file', 'usuario', 'Documentos')
    software_usuario = fields.Many2many('sitecnet.software',
                                'software_usuarios_rel',
                                'usuario_id',
                                'software_id',
                                'Software')
    accesos_usuario = fields.One2many('sitecnet.cuentas', 'usuario', string='Accesos', copy=True, auto_join=True)
