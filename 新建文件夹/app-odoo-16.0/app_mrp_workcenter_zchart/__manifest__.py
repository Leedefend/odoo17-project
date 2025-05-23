# -*- coding: utf-8 -*-

# Created on 2019-05-26
# author: 欧度智能，https://www.odooai.cn
# email: 300883@qq.com
# resource of odooai
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

# Odoo12在线用户手册（长期更新）
# https://www.odooai.cn/documentation/user/12.0/zh_CN/index.html

# Odoo12在线开发者手册（长期更新）
# https://www.odooai.cn/documentation/12.0/index.html

# Odoo10在线中文用户手册（长期更新）
# https://www.odooai.cn/documentation/user/10.0/zh_CN/index.html

# Odoo10离线中文用户手册下载
# https://www.odooai.cn/odoo10_user_manual_document_offline/
# Odoo10离线开发手册下载-含python教程，jquery参考，Jinja2模板，PostgresSQL参考（odoo开发必备）
# https://www.odooai.cn/odoo10_developer_document_offline/

##############################################################################
#    Copyright (C) 2009-TODAY odooai.cn Ltd. https://www.odooai.cn
#    Author: Ivan Deng，300883@qq.com
#    You can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#    See <http://www.gnu.org/licenses/>.
#
#    It is forbidden to publish, distribute, sublicense, or sell copies
#    of the Software or modified copies of the Software.
##############################################################################

{
    'name': "MRP Workcenter zChart Parent Child Hierarchy,工作中心分级",
    'version': '17.0.0.1',
    'author': 'odooai.cn',
    'category': 'Extra tools',
    'website': 'https://www.odooai.cn',
    'license': 'LGPL-3',
    'sequence': 2,
    'price': 0.00,
    'currency': 'EUR',
    'images': ['static/description/banner.png'],
    'depends': [
        'mrp_workorder',
    ],
    # 不要误装别的，避免冲突
    'excludes': [
        'app_mrp_production_chart',
    ],
    'summary': """
    Odoo App of odooai.cn
    """,
    'description': """    
    Support Odoo 16, 15, 14, 13, 12, 11, Enterprise and Community Edition
    1. D
    2.     
    11. Multi-language Support.
    12. Multi-Company Support.
    ==========
    1. 
    2. 
    11. 多语言支持
    12. 多公司支持
    """,
    'data': [
        # 'security/*.xml',
        # 'security/ir.model.access.csv.csv',
        # 'data/*.xml',
        'views/mrp_workcenter_views.xml',
    ],
    'qweb': [
        'static/src/xml/*.xml',
    ],
    'demo': [],
    'test': [],
    'css': [],
    'js': [],
    # 'pre_init_hook': 'pre_init_hook',
    # 'post_init_hook': 'post_init_hook',
    # 'uninstall_hook': 'uninstall_hook',
    'installable': True,
    'application': True,
    'auto_install': False,
}
