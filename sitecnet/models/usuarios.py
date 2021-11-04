# -*- coding: utf-8 -*-

from odoo import models, fields, api

class usuarios(models.Model):
    _name = 'sitecnet.usuarios'
    _rec_name = 'name'

    def _get_file_name(self):
        return self.content_fname or "NewFile"

    def _get_file_directory(self):
        return self.env.ref("muk_dms.directory").id

    name = fields.Char('Nombre del Usuario', required=True, )
    documentos = fields.One2many('muk_dms.file', 'usuarios', string='Documentos')  # Configurar,
    cliente = fields.Many2one('sitecnet.clientes', 'Cliente', required=True, ) ##Uso interno
    procesos = fields.Many2one('sitecnet.rutinas', 'Procesos')
    programas = fields.Text('Programas Permitidos') #evaluar si poner casillas de verificacion
    correo = fields.Char('Correo', required=True, )
    puesto = fields.Char('Puesto', required=True, )
    telefono = fields.Char('Telefono', required=True, )
    equipo = fields.One2many('sitecnet.equipos', 'usuarios', string='Equipo')
    tickets = fields.One2many('sitecnet.helpdesk', 'usuario', string='Reportes', required=True, )
    cuentas = fields.One2many('sitecnet.cuentas', 'usuario', string='Cuentas', copy=True, auto_join=True)
    responsiva = fields.Binary('Responsiva')
    software = fields.Many2many('sitecnet.software', 
                                'software_usuarios_rel', 
                                'usuario_id', 'software_id', 
                                'Licencias asignadas')  # Configurar
    notas = fields.Text('Notas')
    # Sucursal = fields.Char('Ubicacion', required=True,) Heredado de Cliente

