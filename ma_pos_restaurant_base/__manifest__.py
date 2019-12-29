{
    "name": """POS restaurant base""",
    "summary": """Technical module in POS""",
    "category": "Point of Sale",
    # "live_test_URL": "",
    "images": ['images/pos_restaurant_base.jpg'],
    "version": "12.0.2.0.4",
    "application": False,

    "author": "Mediterranean Apps",
    "support": "mediterranean.apps@gmail.com",
    "website": "",
    "license": "LGPL-3",
    "price": 11.66,
    "currency": "EUR",

    "depends": [
        "pos_restaurant",
    ],
    "external_dependencies": {"python": [], "bin": []},
    "data": [
        "views/template.xml",
    ],
    "qweb": [
    ],
    "demo": [
    ],

    "post_load": None,
    "pre_init_hook": None,
    "post_init_hook": None,

    "auto_install": False,
    "installable": True,
}
