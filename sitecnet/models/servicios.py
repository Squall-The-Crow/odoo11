# -*- coding: utf-8 -*-

from odoo import models, fields, api

class servicios(models.Model):
    _name = 'sitecnet.servicios'
    _rec_name = 'name'

    name = fields.Char('Descripcion corta', required=True,)
    empresa = fields.Many2one('res.partner', string='Clientes', ondelete='cascade', select=True, domain=[('is_company', '=', True)])
    usuario = fields.Many2one('res.partner', 'Usuario')#poner filtro y dominio
    detalles = fields.Text('Detalles del Servicio')
    cantidad = fields.Integer('Cantidad de eventos contratados')
    intervalo = fields.Integer('Intervalo en dias')
    fcomienzo = fields.Date('Inicio de rutinas')
    ffinal = fields.Date('Final del contrato')
    frevision = fields.Datetime('Revision de servicios')    
    revisado = fields.Boolean('Procedimiento Revisado')
    rutinas_creadas = fields.Boolean('rutinas creadas')
    rutinas = fields.One2many('sitecnet.rutinas', 'servicio', string='Rutinas programadas', copy=True, auto_join=True)
    equipos = fields.One2many('sitecnet.equipos', 'poliza', string='Equipos amparados', copy=True, auto_join=True)
    #Crear boton y proceso de rutinas

    @api.multi
    def create_rutinas(self):
        vals = {
            'name': self.name,
            'empresa': self.empresa.id,
            'fecha': self.fcomienzo
        }
        self.env['sitecnet.rutinas'].create(vals)

class categoria_servicios(models.Model):
    _name = 'sitecnet.categoria_servicios'
    _rec_name = 'name'

    name = fields.Char('Categoria')

class rutinas(models.Model):
    _name = 'sitecnet.rutinas'
    _rec_name = 'name'

    name = fields.Char('Descripcion corta', required=True,)
    empresa = fields.Many2one('res.partner', string='Clientes', ondelete='cascade', select=True, domain=[('is_company', '=', True)])
    usuario = fields.Many2one('res.partner', 'Encargado')#poner filtro y dominio
    tecnico = fields.Many2one ('res.users', 'Tecnico asignado')#poner filtro de tecnico
    fecha = fields.Datetime('Fecha programada de actividad')
    servicio = fields.Many2one ('sitecnet.servicios', 'Servicio de Origen')    
    validacion = fields.Text('Comentarios de validacion')
    calificacion = fields.Selection([('bueno', 'Bueno'),
                               ('regular', 'Regular'),
                               ('malo', 'Malo'),
                               ], string='Calificacion de actividad', default='bueno')
    resultado = fields.Text('Resultado de la actividad')
    estado = fields.Selection([('pendiente', 'Pendiente'),
                                    ('curso', 'En Curso'),
                                    ('cancelado', 'cancelado'),
                                    ('programado', 'programado'),
                                    ('atrasado', 'Atrasado'),
                                    ('validado', 'Validado'),
                                    ], string='Estado', default='programado')
    usuarios = fields.Many2many('res.partner',
                              'rutinas_usuarios_rel',
                              'rutinas_id',
                              'usuarios_id',
                              string='Usuarios asignados')
    equipo = fields.Many2many('sitecnet.equipos',
                              'equipos_rutinas_rel',
                              'rutinas_id',
                              'equipos_id',
                              string='Equipos involucrados')