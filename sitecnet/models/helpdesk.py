# -*- coding: utf-8 -*-
from odoo import models, fields, api
from datetime import timedelta

class helpdesk(models.Model):
    _inherit = "website.support.ticket"

    ubicacion = fields.Selection([('remoto', 'Remoto'),
                               ('oficina', 'Visita a Oficina'),
                               ('domicilio', 'Visita a Domicilio'),
                               ], string='Ubicacion del soporte', default='remoto')
    tipo = fields.Selection([('falla', 'Falla o Error'),
                                   ('consulta', 'Ayuda o consulta'),
                                   ('procedimiento', 'Solicitud de procedimiento / configuracion'),
                                    ('solicitud de conferencia', 'Solicitud de conferencia / capacitacion'),
                                   ], string='Tipo de soporte', default='consulta')
    empresa = fields.Many2one('res.partner', string='Cliente')#domain=[('is_company', '=', True)]
    usuario = fields.Many2one('res.partner', string='Usuario con problemas') #domain= [('partner_ids','in', empresa.id)]
    equipo = fields.Many2one('sitecnet.equipos', 'Equipo con problemas') #poner domain domain=[('partner.id', '=', usuario.id)]
    reportado = fields.Many2one('res.users', string='Reportado Por', default=lambda self: self.env.user)
    conexion = fields.Char('Conexion Remota')
    actividades = fields.One2many('sitecnet.actividades', 'reporte', string='Actividades', copy=True, auto_join=True)
    calificacion = fields.Selection([('bueno', 'Bueno'),
                               ('regular', 'Regular'),
                               ('malo', 'Malo'),
                               ], string='Calificacion de soporte', default='bueno')
    telefono = fields.Char('Telefono de contacto')
    cel = fields.Char('Movil de contacto')
    elevado = fields.Boolean('Elevado')

    @api.onchange('equipo')
    def _onchange_equipo(self):
        self.conexion = self.equipo.ID_remoto

    @api.onchange('usuario')
    def _onchange_partner_id2(self):
        self.telefono = self.partner_id.mobile
        self.cel = self.partner_id.phone

helpdesk()

class actividades(models.Model):
    _name = 'sitecnet.actividades'
    _description = 'Actividades de soporte'
    _order = 'name'

    def _default_fecha(self):
        return fields.Date.context_today(self)

    name = fields.Char('Actividad', required=True, readonly=False, store=True)
    fecha = fields.Date('Fecha', default=_default_fecha, required=True)
    resumen = fields.Text('Resumen de actividad', required=True)
    diagnostico = fields.Text('Diagnostico')
    reporte = fields.Many2one('website.support.ticket', 'Reporte de Origen') # poner automatico
    fecha_programada = fields.Date('Hora de actividad', default=_default_fecha)
    solucion = fields.Selection([('si', 'Si'),
                               ('no', 'No'),
                                ('na', 'No Aplica'),
                               ], string='Resolvio la situacion?', default='si')