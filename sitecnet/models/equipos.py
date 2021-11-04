# -*- coding: utf-8 -*-

from odoo import models, fields, api

class equipos(models.Model):
    _name = 'sitecnet.equipos'
    _rec_name = 'serie'

    marca = fields.Char('Marca')
    modelo = fields.Char('Modelo')
    serie = fields.Char('Numero de Serie', required=True)
    tipo = fields.Many2one('sitecnet.tipo_equipo', 'Tipo', required=True,)
    subtipo = fields.Many2one('sitecnet.subtipo_equipo', 'Subtipo', required=True,)
    status = fields.Selection([('activo', 'Activo'),
                               ('fo', 'Fuera de operacion'),
                               ('mto', 'En mantenimiento'),
                               ('baja', 'Equipo fuera de servicio'),
                               ], string='Estado', default='activo')
    ip = fields.Char('IP')
    localizacion = fields.Char('Localizacion Fisica') #pensar en automatico direccion o sucursal en funcion de usuario o empresa
    descripcion = fields.Char('Descripcion corta')
    fecha_compra = fields.Date('Fecha de Compra')
    fin_garantia = fields.Date('Fin de Garantia')
    fecha_fin = fields.Date('Fecha de final de vida Util', required=True,)
    factura_cliente = fields.Many2one('muk_dms.file', 'Factura Cliente')
    factura_interna = fields.Many2one('muk_dms.file', 'Factura Interna')
    renta = fields.Boolean('Equipo en renta')
    #cuentas = fields.Many2many('sitecnet.cuentas',
     #                          'sitecnet_equipos_rel',
      #                         string='Cuentas', )
    dominio = fields.Boolean('Es miembro de dominio')
    nombre_dominio= fields.Char('Nombre de Dominio') # If dominio True
    configuracion = fields.Char('Ubicacion de Configuracion')
    drivers = fields.Char('Ubicacion de Drivers')
    observaciones = fields.Text('Observaciones')
    usuarios = fields.Many2one('sitecnet.usuarios', string='Usuarios')
    licencias = fields.Many2many('sitecnet.software',
                              'software_equipos_rel',
                              'equipos_id',
                              'software_id',
                              string='Licencias')
    helpdesk = fields.One2many('sitecnet.helpdesk', 'equipo', string='Reportes', copy=True, auto_join=True)
    cuentas = fields.One2many('sitecnet.cuentas', 'equipo', string='Cuentas asociadas', copy=True, auto_join=True)
    equipo = fields.Many2one('sitecnet.equipos', string='Equipos', index=True, ondelete='cascade')
    componentes = fields.One2many('sitecnet.equipos', 'equipo')
    # poliza heredada de cliente
    cliente = fields.Many2one('sitecnet.clientes', string='Cliente')
    # responsiva heredada de usuario
    procesador_linea = fields.Char('Linea de Procesador')
    procesador_modelo = fields.Char('Modelo de Procesador')
    dd_tipo = fields.Char('Tecnologia DD')
    dd_capacidad = fields.Char('Capacidad DD')
    memoria_capacidad = fields.Char('Capacidad Memoria')
    memoria_tipo = fields.Char('Tecnologia memoria')
    procesos = fields.Many2one('sitecnet.rutinas', 'Procesos')

class tipo(models.Model):
    _name = 'sitecnet.tipo_equipo'
    _rec_name = 'name'

    name = fields.Char('Tipo de Equipo', required=True,)

class subtipo(models.Model):
    _name = 'sitecnet.subtipo_equipo'
    _rec_name = 'name'

    name = fields.Char('subtipo', required=True)
    tipo = fields.Many2one('sitecnet.tipo_equipo', string='Tipo')



