from odoo import models, fields, api
from datetime import timedelta

class helpdesk(models.Model):
    _name = 'sitecnet.helpdesk'
    _rec_name = 'name'
###Funcion Fecha automatica######
    def _default_fecha(self):
        return fields.Date.context_today(self)

    ###Funcion Vigencia automatica######

    def _default_vigencia(self):
        today_str = fields.Date.context_today(self)
        today = fields.Date.from_string(today_str)
        expected = today + timedelta(days=1)
        return fields.Date.to_string(expected)


    name = fields.Char(string='Ticket', required=True, copy=False, readonly=True, index=True,
                   default=lambda self: ('New'))
    fecha = fields.Date('Fecha', default=_default_fecha, required=True)
    tr = fields.Date('Tiempo de respuesta maximo', default=_default_vigencia)
    importancia = fields.Selection([('alta', 'Alta'),
                                    ('media', 'Media'),
                                    ('baja', 'Baja'),
                                    ], string='Importancia', default='baja')
    estado = fields.Selection([('abierto', 'Abierto'),
                                    ('cerrado', 'Cerrado'),
                                    ('cancelado', 'Cancelado'),
                                    ('paprobracion', 'Pendiente de aprobacion'),
                                    ('aceptado', 'Aceptado'),
                                    ('atrasado', 'Atrasado'),
                                    ], string='Estado', default='abierto')
    ubicacion = fields.Selection([('remoto', 'Remoto'),
                               ('oficina', 'Visita a Oficina'),
                               ('domicilio', 'Visita a Domicilio'),
                               ], string='Ubicacion del soporte', default='remoto')
    tipo = fields.Selection([('falla', 'Falla o Error'),
                                   ('consulta', 'Ayuda o consulta'),
                                   ('procedimiento', 'Solicitud de procedimiento / configuracion'),
                                    ('solicitud de conferencia', 'Solicitud de conferencia / capacitacion'),
                                   ], string='Tipo de soporte', default='consulta')
    reportado = fields.Many2one('res.users', string='Reportado Por', default=lambda self: self.env.user)
    usuario = fields.Many2one('sitecnet.usuarios', 'Usuario con problemas', required=True)
    cliente = fields.Many2one('sitecnet.clientes', 'cliente', related='usuario.cliente', readonly=True, store=True ) #revisar
    equipo = fields.Many2one('sitecnet.equipos', 'Equipo con problemas', required=True) #poner domain
    descripcion = fields.Text('Descripcion', required=True)
    tiempo_total = fields.Float('Tiempo total de servicio')
    resultado = fields.Text('acciones y resultado')
    actividades = fields.One2many('sitecnet.actividades', 'name', string='Actividades', copy=True, auto_join=True)
    evidencia = fields.One2many('sitecnet.evidencia', 'name', string='Evidencia', copy=True, auto_join=True)
    reinsidencia = fields.Boolean('Reinsidencia')
    calificacion = fields.Selection([('bueno', 'Bueno'),
                               ('regular', 'Regular'),
                               ('malo', 'Malo'),
                               ], string='Calificacion de soporte', default='bueno')
    comentarios = fields.Text('Comentarios')
    categoria = fields.Many2one('sitecnet.helpdesk.categoria', 'Categoria Reporte')
    subcategoria = fields.Many2one('sitecnet.helpdesk.subcategoria', 'Subcategoria')
    cerrado = fields.Date('Fecha de cierre')
    #tecnico = fields.Many2one('res.users', 'Tecnico asignado')
    responsable = fields.Char('Responsable de siguiente accion')
    correo = fields.Char('Correo de contacto', related='usuario.correo')
    direccion = fields.Char('Direccion de soporte', related='cliente.direccion')
    telefono = fields.Char('Telefono de contacto', related='usuario.telefono')
    elevado = fields.Boolean('Elevado')
    #cotizacion = fields.Many2one('sitecnet.cotizacion_tickets', string='Costo de Reparacion')

#######Automatizacion de nombre consecutivo#########
    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].next_by_code('helpdesk') or ('New')
        res = super(helpdesk, self).create(vals)
        return res

class Actividades(models.Model):
    _name = 'sitecnet.actividades'
    _description = 'Actividades de soporte'
    _order = 'name'

    def _default_fecha(self):
        return fields.Date.context_today(self)

    name = fields.Char('Actividad', required=True, readonly=False, store=True)
    fecha = fields.Date('Fecha', default=_default_fecha, required=True)
    resumen = fields.Text('Resumen de actividad', required=True)
    diagnostico = fields.Text('Diagnostico')
    reporte = fields.Many2one('sitecnet.helpdesk', 'Reporte de Origen')
    fecha_programada = fields.Date('Fecha programada de respuesta', default=_default_fecha)
    solucion = fields.Selection([('si', 'Si'),
                               ('no', 'No'),
                                ('na', 'No Aplica'),
                               ], string='Resolvio la situacion?', default='si')


class Evidencia(models.Model):
    _name = 'sitecnet.evidencia'
    _description = 'Evidencia de Reportes'
    _order = 'name'

    name = fields.Char('Descripcion', required=True, readonly=False, store=True)
    evidencia = fields.Binary('Documento', ondelete='restrict', required=True)
    reporte = fields.Many2one('sitecnet.helpdesk', 'Reporte de Origen')

class Categoria(models.Model):
    _name = 'sitecnet.helpdesk.categoria'
    _description = 'Categoria de reportes'
    _order = 'name'
    name = fields.Char('Categoria')

class Subcategoria(models.Model):
    _name = 'sitecnet.helpdesk.subcategoria'
    _description = 'Subcategoria de Reportes'
    _order = 'name'
    name = fields.Char('Subcategoria')
    categoria = fields.Many2one('sitecnet.helpdesk.categoria', string='Categoria principal')

    ###Campos o funciones pendientes por definir#####
    #empresa
    #ubicacion
    #Historial de conversaciones
    #Poner marca de tiempo en cerrado
    #Filtro de usuario por equipo
    #Default datos de contacto de usuario
    #Hacer proceso de calificacion y comentarios


