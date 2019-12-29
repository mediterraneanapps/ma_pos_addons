# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).
{
    "name": """Lock POS Screen""",
    "summary": """Users/Cashiers can unlock POS screen by scanning their barcode or using security PIN""",
    "category": "Point of Sale",
    "images": ["images/pos_logout_main.png"],
    "version": "12.0.1.0.0",
    "application": False,

    "author": "Mediterranean Apps",
    "support": "mediterranean.apps@gmail.com",
   # "website": "",
    "license": "LGPL-3",
    "price": 13.00,
    "currency": "EUR",

    "depends": [
        "ma_pos_pin",
    ],
    "external_dependencies": {"python": [], "bin": []},
    "data": [
        "views/pos_logout.xml",
    ],
    "qweb": [
        "static/src/xml/pos.xml"
    ],
    "demo": [
    ],

    "post_load": None,
    "pre_init_hook": None,
    "post_init_hook": None,

    "auto_install": False,
    "installable": True,

    "demo_title": "Lock POS Screen",
    "demo_addons": [
    ],
    "demo_addons_hidden": [
    ],
    "demo_url": "pos-logout",
    "demo_summary": "Users/Cashiers can unlock POS screen by scanning their barcode or using security PIN",
    "demo_images": [
        "images/pos_logout_main.png",
    ]
}
