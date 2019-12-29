{
    "name": """POS Print Method""",
    "summary": """Choose print method for order printing in POS""",
    "category": "Point of Sale",
    "images": ["images/pm1.png"],
    "version": "12.0.1.0.1",
    "application": False,

    "author": "Mediterranean Apps",
    "support": "mediterranean.apps@gmail.com",
    "website": "",
    "license": "LGPL-3",
    "price": 11.33,
    "currency": "EUR",

    "depends": [
        "pos_restaurant",
        "ma_pos_restaurant_base",
    ],
    "external_dependencies": {"python": [], "bin": []},
    "data": [
        "views/template.xml",
        "views/view.xml",
    ],
    "qweb": [
    ],
    "demo": [
        "data/restaurant_printer_demo.xml",
    ],

    "post_load": None,
    "pre_init_hook": None,
    "post_init_hook": None,

    "auto_install": False,
    "installable": True,
}
