{
    "name": """Merge POS Orders""",
    "summary": """Merge POS orders into a single order""",
    "category": "Point of Sale",
    "images": ["images/pos_order_merge_main.jpg"],
    "version": "11.0.1.0.0",
    "application": False,

    "author": "Mediterranean Apps",
    "support": "mediterranean.apps@gmail.com",
   # "website": "",
    "license": "LGPL-3",
    "price": 23.00,
    "currency": "EUR",

    "depends": [
        "pos_restaurant",
    ],
    "external_dependencies": {"python": [], "bin": []},
    "data": [
        "views/pos_order_merge_template.xml",
        "views/pos_config_view.xml",
    ],
    "qweb": [
        "static/src/xml/merge.xml",
    ],
    "demo": [
    ],

    "post_load": None,
    "pre_init_hook": None,
    "post_init_hook": None,
    "uninstall_hook": None,

    "auto_install": False,
    "installable": True,
}
