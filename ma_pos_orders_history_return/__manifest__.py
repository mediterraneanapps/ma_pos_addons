# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).
{
    "name": """POS Orders Return""",
    "summary": """The module allows to make order returns from POS interface by quick & easy way""",
    "category": "Point of Sale",
    "images": ["images/pos_orders_return_main.jpg"],
    "version": "12.0.1.0.6",
    "application": False,

    "author": "Mediterranean Apps",
    "support": "mediterranean.apps@gmail.com",
    "website": "",
    "license": "LGPL-3",
    "price": 13.00,
    "currency": "EUR",

    "depends": [
        "ma_pos_orders_history",
    ],
    "external_dependencies": {"python": [], "bin": []},
    "data": [
        "views/pos_orders_history_return_view.xml",
        "views/pos_orders_history_return_template.xml",
    ],
    "demo": [
    ],
    "qweb": [
        "static/src/xml/pos.xml",
    ],

    "post_load": None,
    "pre_init_hook": None,
    "post_init_hook": None,
    "uninstall_hook": None,

    "auto_install": False,
    "installable": True,

    "demo_title": "POS Orders Refund",
    "demo_addons": [
    ],
    "demo_addons_hidden": [
    ],
    "demo_url": "pos-orders-return",
    "demo_summary": "The module allows to make order returns from POS interface by convenient way",
    "demo_images": [
        "images/pos_orders_return_main.jpg",
    ]
}
