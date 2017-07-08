# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from odoo.exceptions import UserError


class StockContainer(models.Model):
    _inherit = "mail.thread"
    _name = "stock.container"
    _description = "Container"
    _order = "name desc"

    name = fields.Char(
        string='Container Name', default='/',
        copy=False, required=True,
        help='Name of the Container')
    load = fields.date(
        string='Loading Date', copy=False, required=False)
    sail = fields.Date(
        string='Sailing Date', copy=False, required=False)
    arrival = fields.date(
        string='Arrival Date', copy=False, required=False)
    picking_ids = fields.One2many(
        'stock.picking','container_id',string='Pickings',
        help='Transfers Associated w/ Container')
    cbm = fields.float(
        compute='_container_cbm', store=True, string='CBM',
        copy=False, required=False)

    @api.model
    def create(self, vals):
        if vals.get('name', '/') == '/':
            vals['name'] =  '/'
        return super(StockContainer, self).create(vals)


    @api.depends('picking_ids')
    def _container_cbm(self):
        for record in self:
            #record.cbm = sum(record.picking_ids.filtered(lamda r: r.state != 'cancel').mapped('cbm'))
            for transfer in record.picking_ids:
                container_cbm += transfer.product_id.volume
            record.cbm = container_cbm

class StockPicking(models.Model):
    _inherit = "stock.picking"

    container_id = fields.Many2one(
        'stock.container', string='Container',
        states={'done': [('readonly', True)], 'cancel': [('readonly', True)]},
        help='Transfer Container')
