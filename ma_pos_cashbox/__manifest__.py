{
    "name": """Open CashBox from Backend""",
    "summary": """The module allows to open Cashbox/Cashdrawer from Backend""",
    "category": "Point of Sale",
    "images": ['images/pos_cashbox_main.png'],
    "version": "10.0.1.0.0",
    "application": False,

    "author": "Mediterranean Apps",
    "support": "mediterranean.apps@gmail.com",
   # "website": "",
    "license": "LGPL-3",
    "price": 16.33,
    "currency": "EUR",

    "depends": [
        "point_of_sale",
    ],
    "external_dependencies": {"python": [], "bin": []},
    "data": [
        "views/pos_cashbox_template.xml",
        "views/pos_cashbox_view.xml",
    ],
    "qweb": [
    ],
    "demo": [
    ],

    "post_load": None,
    "pre_init_hook": None,
    "post_init_hook": None,
    "uninstall_hook": None,

    "auto_install": False,
    "installable": True,

    "demo_title": "Open CashBox from Backend",
    "demo_addons": [
    ],
    "demo_addons_hidden": [
    ],
    "demo_url": "pos-cashbox",
    "demo_summary": "The module allows to open the CashBox from Backend",
    "demo_images": [
        "images/pos_cashbox_main.png",
    ]
}
