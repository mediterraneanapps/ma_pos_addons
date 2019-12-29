# License LGPL-3.0 (https://www.gnu.org/licenses/lgpl.html).
{
    "name": """POS Cashier Select""",
    "summary": """Forced choose a cashier before switching to payment screen""",
    "category": "Point of Sale",
    "images": ['images/pos_cashier_select.png'],
    "version": "12.0.1.0.2",
    "application": False,

    "author": "Mediterranean Apps",
    "support": "mediterranean.apps@gmail.com",
    "website": "",
    "license": "LGPL-3",
    "price": 13.00,
    "currency": "EUR",

    "depends": [
        "point_of_sale",
    ],
    "external_dependencies": {"python": [], "bin": []},
    "data": [
        "views/views.xml",
    ],
    "qweb": [
        "static/src/xml/pos.xml",
    ],

    "post_load": None,
    "pre_init_hook": None,
    "post_init_hook": None,

    "auto_install": False,
    "installable": True,
}
