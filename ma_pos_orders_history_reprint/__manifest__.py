# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).
{
    "name": """Reprint POS Orders Receipt""",
    "summary": """Reprint receipts of paid POS orders""",
    "category": "Point of Sale",
    "images": ["images/pos_orders_reprint_main.png"],
    "version": "12.0.1.0.4",
    "application": False,

    "author": "Mediterranean Apps",
    "support": "mediterranean.apps@gmail.com",
    "website": "",
    "license": "LGPL-3",
    "price": 6.66,
    "currency": "EUR",

    "depends": [
        "ma_pos_orders_history",
    ],
    "external_dependencies": {"python": [], "bin": []},
    "data": [
        "security/ir.model.access.csv",
        "views/template.xml",
        "views/view.xml",
        "data/base_action_rule.xml",
    ],
    "demo": [
    ],
    "qweb": [
        "static/src/xml/main.xml",
    ],

    "post_load": None,
    "pre_init_hook": None,
    "post_init_hook": None,
    "uninstall_hook": None,

    "auto_install": False,
    "installable": True,

    "demo_title": "Reprint POS Orders Receipt",
    "demo_addons": [
    ],
    "demo_addons_hidden": [
    ],
    "demo_url": "pos-orders-reprint",
    "demo_summary": "Reprint receipts of paid POS orders",
    "demo_images": [
        "images/pos_orders_reprint_main.png",
    ]
}
