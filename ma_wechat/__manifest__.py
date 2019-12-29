# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).
{
    "name": """WeChat API""",
    "summary": """Technical module to integrate Odoo with WeChat""",
    "category": "Hidden",
    "images": [],
    "version": "12.0.1.0.1",
    "application": False,

    "author": "Mediterranean Apps",
    "support": "mediterranean.apps@gmail.com",
    "website": "",
    "license": "LGPL-3",
    "price": 50.00,
    "currency": "EUR",

    "depends": [
        'product',
        'account',
        'ma_qr_payments',
    ],
    "external_dependencies": {"python": [
        'wechatpy',
    ], "bin": []},
    "data": [
        "views/account_menuitem.xml",
        "views/wechat_micropay_views.xml",
        "views/wechat_order_views.xml",
        "views/wechat_refund_views.xml",
        "views/account_journal_views.xml",
        "data/ir_sequence_data.xml",
        "security/ir.model.access.csv",
    ],
    "qweb": [],

    "auto_install": False,
    "installable": True,
}
