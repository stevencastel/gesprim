# -*- coding: utf-8 -*-
{
    'name': "difodoo_fichiers_base",

    'summary': """
        difodoo_fichiers_base""",

    'description': """
        Surcharge des fichiers de base
    """,

    'author': "Difference informatique",
    'website': "http://www.pole-erp-pgi.fr",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'difodoo',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale','product','sale_stock'],

    # always loaded
    'data': [
        "views/di_inh_product_view.xml",
        "views/di_inh_res_partner_view.xml",        
        "views/di_tables_view.xml",
        "wizard/di_wiz_referencer_article.xml",
        "wizard/di_product_pack_wizard.xml",
        "wizard/di_generer_tarifs_wizard.xml"
        # 'security/ir.model.access.csv',
      
    ],
    # only loaded in demonstration mode
    'demo': [
       
    ],
}