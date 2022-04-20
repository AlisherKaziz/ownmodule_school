# -*- coding: utf-8 -*-
{
    'name': "om_school",
    'summary': "School Navigation Soft",
    'author': "ALisherK",
    'website': "http://www.yourcompany.com",
    'category': 'Tools',
    'version': '0.1',
    'depends': [],
    'data': [
        'security/ir.model.access.csv',
        'views/tutors.xml'
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'post_init_hook': '_auto_install_l10n',
    'license': 'LGPL-3',
}
