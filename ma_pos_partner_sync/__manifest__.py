# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).
{
    "name": """Sync Partners in POS""",
    "summary": """Instant updates of the partner data in POS""",
    "category": "Point of Sale",
    "images": ["images/pos_partner_sync.jpeg"],
    "version": "12.0.2.0.1",
    "application": False,

    "author": "IMediterranean Apps",
    "support": "mediterranean.apps@gmail.com",
    "website": "",
    "license": "LGPL-3",
    "price": 16.33,
    "currency": "EUR",

    "depends": [
        "point_of_sale",
        "ma_pos_longpolling",
    ],
    "external_dependencies": {"python": [], "bin": []},
    "data": [
        "views/assets.xml",
        "views/pos_config.xml",
    ],

    "post_load": None,
    "pre_init_hook": None,
    "post_init_hook": None,
    "uninstall_hook": None,

    "auto_install": False,
    "installable": True,

    "demo_title": "Sync Partner data in POS",
    "demo_addons": [
    ],
    "demo_addons_hidden": [
    ],
    "demo_url": "pos-partner-sync",
    "demo_summary": "Update the partner data in POS instantly",
    "demo_images": [
        "images/pos_partner_sync_main.png",
    ]
}
