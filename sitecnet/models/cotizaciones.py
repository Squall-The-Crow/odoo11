# -*- coding: utf-8 -*-

from odoo import models, fields, api

class cotizacion_tickets(models.Model):
    _name = 'sitecnet.cotizacion_tickets'
    _rec_name = 'name'

    name = fields.Char('Cotizacion', required=True)
    linea_cotizacion = fields.One2many('sitecnet.cotizacion_tickets.linea', 'name', string='Concepto', copy=True, auto_join=True)
    subtotal = fields.Float('Subtotal', dp.get_precision('Precio'), store=True, compute="_costo_total")
    IVA = fields.Float('IVA', dp.get_precision('Precio'), store=True, compute="_costo_total")
    total = fields.Float('Total', dp.get_precision('Precio'), store=True, compute="_costo_total")

class cotizacion_tickets_linea(models.Model):
    _name = 'sitecnet.cotizacion_tickets.linea'
    _rec_name = 'name'

    name = fields.Char('descripcion', required=True)
    refaccion = fields.Many2one('sitecnet.catalogo', string='Refaccion')
    cantidad = fields.Float(string='Quantity', digits=dp.get_precision('Precio'), required=True,
                            default=1.0)
    subtotal = fields.Float(compute='_compute_amount', digits=dp.get_precision('Precio'), string='Subtotal')
    precio_line = fields.Float(compute='_compute_amount', string='Precio_line', required=True,
                               digits=dp.get_precision('Precio'))
