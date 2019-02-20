# -*- coding: utf-8 -*-
{
    'name': 'testapp',

    'summary': 'This is an auto write program for wind.',
    'description': 'Manage library book catalogue and lending.',
    'author': 'Zhirun Company',
    'website': "http://www.cr-power.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Tools',
    'version': '12.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
         # 'security/ir.model.access.csv',
         # 'security/test_security.xml',
         # 'views/project_view.xml',
         # 'views/project_form_view.xml',
           'views/test_menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}