# -*- coding: utf-8 -*-

# Created on 2018-08-15
# author: 欧度智能，https://www.odooai.cn
# email: 300883@qq.com
# resource of odooai
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

# Odoo在线中文用户手册（长期更新）
# https://www.odooai.cn/documentation/user/10.0/zh_CN/index.html

# Odoo10离线中文用户手册下载
# https://www.odooai.cn/odoo10_user_manual_document_offline/
# Odoo10离线开发手册下载-含python教程，jquery参考，Jinja2模板，PostgresSQL参考（odoo开发必备）
# https://www.odooai.cn/odoo10_developer_document_offline/
# description:

{
    'name': "Stock Superbar ztree, parent children tree",
    'version': '17.0.0.1',
    'author': 'odooai.cn',
    'category': 'Warehouse',
    'website': 'https://www.odooai.cn',
    'live_test_url': 'https://demo.odooapp.cn',
    'license': 'LGPL-3',
    'sequence': 2,
    'summary': """
    Use for parent children tree list select navigator. stock location tree, filter by parent location.
    ztree widget.
    """,
    'description': """
    zTree widget.
    Advance search with real parent children tree, ListView or KanbanView ,
    eg: Product category tree ,Department tree, stock location tree.
    超级方便的查询，树状视图。
    """,
    'price': 0.00,
    'currency': 'EUR',
    'depends': [
        'stock',
        'stock_picking_batch',
    ],
    'images': ['static/description/banner.gif'],
    'data': [
        'views/stock_location_views.xml',
        'views/stock_picking_views.xml',
        'views/stock_picking_batch_views.xml',
        'views/stock_picking_type_views.xml',
        'views/stock_warehouse_orderpoint_views.xml',
        'views/stock_rule_views.xml',
        'views/stock_lot_views.xml',
        # todo: 以下两个模型调整了
        # 'views/stock_location_route_views.xml',
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
    'post_init_hook': 'post_init_hook',
    'installable': True,
    'application': True,
    'auto_install': False,
}
