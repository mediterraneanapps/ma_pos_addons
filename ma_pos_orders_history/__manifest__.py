# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).
{
    "name": "POS Orders History",
    "summary": """See all paid orders from special menu in POS""",
    "category": "Point of Sale",
    "images": ['images/pos_orders_history_main.png'],
    "version": "12.0.1.2.1",
    "application": False,

    "author": "Mediterranean Apps",
    "support": "mediterranean.apps@gmail.com",
    "website": "",
    "license": "LGPL-3",
    "price": 19.66,
    "currency": "EUR",

    "depends": [
        "base_automation",
        "ma_pos_longpolling",
    ],
    "external_dependencies": {"python": [], "bin": []},
    "data": [
        "views/pos_orders_history_view.xml",
        "views/pos_orders_history_template.xml",
        "data/base_action_rule.xml",
    ],
    "qweb": [
        "static/src/xml/pos.xml",
    ],
    "demo": [
    ],

    "post_load": None,
    "pre_init_hook": None,
    "post_init_hook": None,

    "auto_install": False,
    "installable": True,

    "demo_title": "POS Orders History",
    "demo_addons": [
    ],
    "demo_addons_hidden": [
    ],
    "demo_url": "pos-orders-history",
    "demo_summary": "See all paid orders from special menu in POS",
    "demo_images": [
        "images/pos_orders_history_main.png",
    ]
}
