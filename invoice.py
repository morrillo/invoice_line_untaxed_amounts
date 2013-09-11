# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (c) 2009-2010 Open UnIT (http://www.openunit.com.ar) All Rights Reserved.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp.osv import fields,osv
import openerp.addons.decimal_precision as dp

from tools import config


class account_invoice_line(osv.osv):
    _inherit = "account.invoice.line"
    _description = "Untaxed amounts in invoice lines"

    #def _amount_line(self, cr, uid, ids, prop, unknow_none,unknow_dict):
    #    res = {}
    #    cur_obj=self.pool.get('res.currency')
    #    for line in self.browse(cr, uid, ids):
    #        if line.invoice_id:
    #            res[line.id] = line.price_unit * line.quantity * (1-(line.discount or 0.0)/100.0) \
    #                         + line.untaxed_amount
    #            cur = line.invoice_id.currency_id
    #            res[line.id] = cur_obj.round(cr, uid, cur, res[line.id])
    #        else:
    #            res[line.id] = round(line.price_unit * line.quantity * (1-(line.discount or 0.0)/100.0) \
    #                         + line.untaxed_amount,int(config['price_accuracy']))
    #    return res

    _columns = {
        'untaxed_amount': fields.float('Untaxed amount', digits_compute=dp.get_precision('Account')),
        # 'price_subtotal': fields.function(_amount_line, method=True, string='Subtotal',store=True, type="float", digits_compute=dp.get_precision('Account')), 
    }

account_invoice_line()
