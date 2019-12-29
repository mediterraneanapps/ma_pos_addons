# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).
{
    "name": """Available quantity of products in POS""",
    "summary": """Adds available quantity at products in POS""",
    "category": "Point Of Sale",
    "images": [],
    "version": "12.0.1.1.0",
    "application": False,

    "author": "Mediterranean Apps",
    "support": "mediterranean.apps@gmail.com",
    "website": "",
    "license": "LGPL-3",
    "price": 3.00,
    "currency": "EUR",

    "depends": [
        'point_of_sale',
        'stock',
    ],
    "external_dependencies": {"python": [], "bin": []},
    'data': [
        'data.xml',
        'views/views.xml',
    ],
    'qweb': [
        'static/src/xml/pos.xml',
    ],

    "post_load": None,
    "pre_init_hook": None,
    "post_init_hook": None,
    "uninstall_hook": None,

    "auto_install": False,
    "installable": True,
}
