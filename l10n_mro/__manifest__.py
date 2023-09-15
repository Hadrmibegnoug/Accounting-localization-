# -*- coding: utf-8 -*-
{
    'name': "Mauritanie - Accounting",
    'author': "ADVANCED BIZ CONSULTING",
    'category': 'Accounting/Localizations/Account Charts',
    'description': """
        This is the base module to manage the accounting chart for Mauritanie.
        
        Ce Module charge le modèle du plan de comptes standard Mauritanien et permet de
        générer les états comptables aux normes mauritaniennes (Bilan, CPC (comptes de
        produits et charges), balance générale à 6 colonnes, Grand livre cumulatif...).
    """,

    'website': "https://www.abc.mr/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'account', 'account_accountant'],

    # always loaded
    'data': [
        'data/l10n_mauritania_chart_data.xml',
        'data/account_tax_group_data.xml',
        'data/account_tax_report_data.xml',
        'data/account_tax_data.xml',
        'data/account_chart_template_data.xml',
        # 'security/ir.model.access.csv',
        # 'views/views.xml',
        # 'views/templates.xml',
        
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
