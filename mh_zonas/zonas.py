   # -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
# Coded by: Said Kuri Nunez (skuri@tantums.com)
##############################################################################

from openerp import models, fields

class mh_zonas(models.Model):
    _name = 'mh.zonas'
    name = fields.Char(string='name')
    shop_ids = fields.One2many(comodel_name='mh.shop',inverse_name='zone_id')


class mh_shop(models.Model):
	_name = 'mh.shop'

	zone_id = fields.Many2one(comodel_name='mh.zonas')
	warehouse_type=fields.Char(string='Warehouse Type')
	warehouse_id = fields.Many2one(comodel_name='stock.warehouse')
	code =fields.Char(string='Code')

