# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).
{
    "name": """Disable options in POS (restaurant extension)""",
    "summary": """Control access to POS restaurant options""",
    "category": "Point of Sale",
    "images": ['images/pos_disable_payment_restaurant.jpg'],
    "version": "10.0.1.0.0",
    "application": False,

    "author": "Mediterranean Apps",
    "support": "mediterranean.apps@gmail.com",
   # "website": "",
    "license": "LGPL-3",
    "price": 9.66,
    "currency": "EUR",

    "depends": [
        "pos_disable_payment",
        "pos_restaurant",
        "web_tour",
    ],
    "external_dependencies": {"python": [], "bin": []},
    "data": [
        "views/template.xml",
        "views/view.xml",
        "views/assets_demo.xml",
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

    "demo_title": "Disable options in POS (restaurant extension)",
    "demo_addons": [
    ],
    "demo_addons_hidden": [
    ],
    "demo_url": "pos-disable-payment-restaurant",
    "demo_summary": "Control access to POS restaurant options",
    "demo_images": [
        "images/pos_disable_payment_restaurant.jpg",
    ]
}
