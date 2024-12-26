# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'My Company Vehicle',
    'version': "17.0.1.0.0",
    'description': """
        Create a vehicle model, with fields computed inheritances, permissions, 
        views and menus, for the Blando technical test.
    """,
    'author': 'Ricardo Sánchez',
    'license': 'LGPL-3',
    'category': 'Custom',
    'depends': [
        'contacts',
    ],
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/my_company_vehicles.xml',
        'views/res_partner_views.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
