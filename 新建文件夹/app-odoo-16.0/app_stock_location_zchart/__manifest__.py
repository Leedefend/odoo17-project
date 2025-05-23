# -*- coding: utf-8 -*-

# Created on 2019-01-04
# author: 欧度智能，https://www.odooai.cn
# email: 300883@qq.com
# resource of odooai
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

# Odoo12在线用户手册（长期更新）
# https://www.odooai.cn/documentation/user/12.0/en/index.html

# Odoo12在线开发者手册（长期更新）
# https://www.odooai.cn/documentation/12.0/index.html

# Odoo10在线中文用户手册（长期更新）
# https://www.odooai.cn/documentation/user/10.0/zh_CN/index.html

# Odoo10离线中文用户手册下载
# https://www.odooai.cn/odoo10_user_manual_document_offline/
# Odoo10离线开发手册下载-含python教程，jquery参考，Jinja2模板，PostgresSQL参考（odoo开发必备）
# https://www.odooai.cn/odoo10_developer_document_offline/


{
    'name': 'Stock Location Chart Hierarchy, 仓库库位多层级结构图',
    'version': '17.0.0.1',
    'author': 'odooai.cn',
    'category': 'Stock',
    'website': 'https://www.odooai.cn',
    'license': 'LGPL-3',
    'sequence': 2,
    'summary': """
    Chart Hierarchy Widget. Hierarchy Chart, Hierarchy Tree for multi level Parent Children relation tree.
    Free for category Hierarchy chart, stock Hierarchy chart. account chart.
    """,
    'description': """    
Need extra paid apps https://www.odoo.com/apps/modules/13.0/app_web_chart_hierarchy/ 
This module extend to show a Hierarchy chart.
(N+1, N+2, direct subordinates)
image: image_field,
desc: descript_field,
direct_sub: children_field, must be one2many,
child_all_count: child_all_count field, count of direct and indirect children.
    """,
    'price': 0.00,
    'currency': 'EUR',
    'depends': [
        'stock',
    ],
    'images': ['static/description/banner.gif'],
    'data': [
        'views/stock_location_views.xml',
    ],
    'demo': [
    ],
    'test': [
    ],
    'css': [
    ],
    'qweb': [
        'static/src/xml/*.xml',
    ],
    'js': [
    ],
    'post_load': None,
    'post_init_hook': None,
    'installable': True,
    'application': True,
    'auto_install': False,
}

