{
    "name": """POS Mobile UI for Waiters""",
    "summary": """Your Restaurant in the Mobile Version""",
    "category": "Point of Sale",
    "images": ["images/pos_mobile_restaurant.png"],
    "version": "12.0.1.3.8",
    "application": False,

    "author": "Mediterranean Apps",
    "support": "mediterranean.apps@gmail.com",
    "website": "",
    "license": "LGPL-3",
    "price": 33.33,
    "currency": "EUR",

    "depends": [
        "ma_pos_restaurant_base",
        "ma_pos_mobile",
    ],
    "external_dependencies": {"python": [], "bin": []},
    "data": [
        "views/pos_mobile_restaurant_template.xml",
        "views/pos_mobile_restaurant_view.xml",
    ],
    "qweb": [
        "static/src/xml/pos.xml",
    ],
    "demo": [
    ],

    "post_load": None,
    "pre_init_hook": None,
    "post_init_hook": None,

    "auto_install": True,
    "installable": True,
}
