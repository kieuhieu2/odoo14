# -*- coding: utf-8 -*-
{
    'name': "module-sale",

    'summary': """
        sale module demo""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",

    'category': 'Uncategorized',
    'version': '0.1',
    'sequence': -100,

    'depends': ['base'],

    'data': [
        'security/ir.model.access.csv',
        'views/order.xml',
        'views/to_invoice.xml',
        'views/reporting.xml',
        'views/product.xml'
    ],
    'demo': [],

    'license': 'LGPL-3',
    'installable': True,
    'application': True,
    'auto_install': False,
}
