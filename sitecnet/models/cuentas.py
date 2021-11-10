# -*- coding: utf-8 -*-

from odoo import models, fields, api

class cuentas(models.Model):
    _name = 'sitecnet.cuentas'
    _rec_name = 'name'
    name = fields.Char('Nombre de usuario', required=True,)
    passw = fields.Char('Password', required=True,)
    acceso = fields.Char('Forma de acceso')
    tipo = fields.Selection([('equipo', 'Equipo'),
                                ('usuario', 'Usuario'),
                                ('servicio', 'Servicio / Recurso'),
                                ('adm', 'Administracion'),
                                ('remoto', 'Acceso Remoto'),
                                ], string='Tipo de cuenta', default='usuario')
    empresa = fields.Many2one('res.partner', string='Empresa', ondelete='cascade', select=True, domain=[('is_company', '=', True)])
    usuario = fields.Many2one('res.partner', string='Usuario', domain=[('parent_id', '=', empresa.id)])
    equipo = fields.Many2one('sitecnet.equipos', string='Equipo asociado')