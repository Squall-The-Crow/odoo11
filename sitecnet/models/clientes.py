# -*- coding: utf-8 -*-

from odoo import models, fields, api


class clientes(models.Model):
    _name = 'sitecnet.clientes'
    _rec_name = 'name'

    name = fields.Char('Cliente', required=True,)
    director = fields.Char('Director General', required=True,)
    contacto = fields.Char('Contacto principal')
    direccion = fields.Char('Direccion principal')
    rfc = fields.Char('RFC')
    servicios = fields.one2many('sitecnet.servicios', 'cliente', string='Servicios contratados', copy=True, auto_join=True)
    rutinas = fields.One2many('sitecnet.rutinas', 'cliente', string='Rutinas y Procesos')
    equipos = fields.One2many('sitecnet.equipos', 'cliente', string='Equipos', copy=True, auto_join=True)
    usuarios = fields.One2many('sitecnet.usuarios', 'cliente', string='Usuarios', copy=True, auto_join=True)
    documentos = fields.One2many('muk_dms.file', 'cliente', 'Documentos')
    software = fields.One2many('sitecnet.software', 'cliente', string='Software', copy=True, auto_join=True)  # Configurar,
    accesos = fields.One2many('sitecnet.cuentas', 'cliente', string='Accesos', copy=True, auto_join=True)  # Configurar,
    notas = fields.Text('Notas')

class servicios(models.Model):
    _name = 'sitecnet.servicios'
    _rec_name = 'name'

    name = fields.Char('Descripción corta', required=True,)
    cliente = fields.Many2one('sitecnet.clientes', string='Clientes')
    detalles = fields.Text('Detalles del Servicio')
    cantidad = fields.Integer('Cantidad de eventos contratados')
    intervalo = fields.Integer('Intervalo en dias')
    fcomienzo = fields.Date('Inicio de rutinas')
    ffinal = fields.Date('Final del contrato')
    frevision = fields.Datetime('Revisión de servicios')
    usuario = fields.Many2one ('res.users', 'Encargado de revisión')#poner filtro de usuario
    revisado = fields.Boolean('Procedimiento Revisado')
    rutinas = fields.One2many('sitecnet.rutinas', 'servicio', string='Rutinas programadas', copy=True, auto_join=True) 
    #Crear boton y proceso de rutinas

class rutinas(models.Model):
    _name = 'sitecnet.rutinas'
    _rec_name = 'name'

    name = fields.Char('Descripción corta', required=True,)
    responsable = fields.Many2one ('res.users', 'Responsable de supervisión')#poner filtro de usuario
    tecnico = fields.Many2one ('res.users', 'Técnico asignado')#poner filtro de tecnico
    fecha = fields.Datetime('Fecha programada de actividad')
    servicio = fields.Many2one ('sitecnet.servicios', 'Servicio de Origen')
    cliente = fields.Many2one('sitecnet.clientes', string='Clientes') #Heredado de servicios
    usuarios = fields.One2many('sitecnet.usuarios', 'procesos', string='Usuarios')
    equipo = fields.One2many('sitecnet.equipos', 'procesos', string='Equipos')
    validacion = fields.Text('Comentarios de validación')
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
                                    ], string='Estado', default='programado')

    ###########Sucursales
    #cliente
    #direccion
    #encargado
    #telefono
    #usuarios