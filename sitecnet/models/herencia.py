# -*- coding: utf-8 -*-

from odoo import fields, models, api

class Users(models.Model):
    _inherit = "muk_dms.file"
    usuarios = fields.Many2one('sitecnet.usuarios', 'Usuario')
    cliente = fields.Many2one('sitecnet.clientes', 'Cliente')

Users()