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
    #facturas
    #rutinas
    equipos = fields.One2many('sitecnet.equipos', 'cliente', string='Equipos', copy=True, auto_join=True)
    usuarios = fields.One2many('sitecnet.usuarios', 'cliente', string='Usuarios', copy=True, auto_join=True)
    #documentos = fields.One2many('Documentos')  # Configurar,
    software = fields.One2many('sitecnet.software', 'cliente', string='Software', copy=True, auto_join=True)  # Configurar,
    accesos = fields.One2many('sitecnet.cuentas', 'cliente', string='Accesos', copy=True, auto_join=True)  # Configurar,
    #tickets = fields.One2many('sitecnet.helpdesk', 'cliente', string='Equipos', copy=True, auto_join=True)  # Configurar,
    notas = fields.Text('Notas')

    ###########Sucursales
    #cliente
    #direccion
    #encargado
    #telefono
    #usuarios