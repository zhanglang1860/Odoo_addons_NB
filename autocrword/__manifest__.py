# -*- coding: utf-8 -*-
{
    'name': 'Autocrword',

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
         'security/autocrword_security.xml',
         'security/ir.model.access.csv',
         'views/autocivil_view.xml',
         'views/civil_view.xml',
         'views/electrical_view.xml',
         'views/wind_view.xml',
         'views/economic_view.xml',
         'views/autowind_view.xml',
         'views/autoeconomic_view.xml',
         'views/autoelectrical_view.xml',
         'views/project_view.xml',
         'views/project_form_view.xml',
         'views/autocrword_menu.xml',
         # 'views/autocrword_rule.xml',
         'reports/autocrword_project_report.xml',
         # 'views/wind_res_view.xml'
         # 'views/windgenerator_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}