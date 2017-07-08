# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Warehouse Management: Containers',
    'version': '1.0',
    'category': 'Warehouse',
    'description': """
This module adds the Container option in warehouse management
================================================================
    """,
    'website': 'https://github.com/JoseMCoronado',
    'depends': ['stock'],
    'data': [
        'views/stock_container_views.xml',
        #'data/stock_container_data.xml',
        'security/ir.model.access.csv',

        #'wizard/stock_picking_to_wave_views.xml',
    ],
    #'demo': [
    #    'data/stock_picking_wave_demo.xml',
    #],
    'installable': True,
}
