{
    "name": """Print certain products on Order Printers""",
    "summary": """Specify certain products to be allowed to print on order printers""",
    "category": "Point of Sale",
    # "live_test_URL": "",
    "images": ['images/pos_order_printer_product_main.png'],
    "version": "12.0.1.0.1",
    "application": False,

    "author": "Mediterranean Apps",
    "support": "mediterranean.apps@gmail.com",
    "website": "",
    "license": "LGPL-3",
    "price": 16.33,
    "currency": "EUR",

    "depends": [
        "pos_restaurant",
        "ma_pos_restaurant_base",
    ],
    "external_dependencies": {"python": [], "bin": []},
    "data": [
        "views/view.xml",
        "views/template.xml",
    ],
    "qweb": [
    ],
    "demo": [
        "data/pos_order_printer_product_demo.xml",
    ],

    "post_load": None,
    "pre_init_hook": None,
    "post_init_hook": None,

    "auto_install": False,
    "installable": True,
}
