# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).
{
    "name": """POS QR Showing in POS""",
    "summary": """Show QR for qr-based payment systems in POS or Customer Screen""",
    "category": "Hidden",
    "images": [],
    "version": "12.0.1.0.0",
    "application": False,

    "author": "Mediterranean Apps",
    "support": "mediterranean.apps@gmail.com",
    "website": "",
    "license": "LGPL-3",
    "price": 13.33,
    "currency": "EUR",

    "depends": [
        "point_of_sale",
    ],
    "external_dependencies": {"python": [], "bin": []},
    "data": [
        "views/assets.xml",
    ],
    "demo": [
    ],
    "qweb": [
        "static/src/xml/pos.xml",
    ],

    "post_load": None,
    "pre_init_hook": None,
    "post_init_hook": None,
    "uninstall_hook": None,

    "auto_install": False,
    "installable": True,
}
