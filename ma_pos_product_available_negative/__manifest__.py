# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).
{
    "name": 'Restrict out-of-stock POS Orders',
    'summary': 'Only supervisor can approve POS Order with out-of-stock product',
    "category": "Point Of Sale",
    "images": [],
    "version": "12.0.1.1.1",
    "application": False,

    "author": "Mediterranean Apps",
    "support": "mediterranean.apps@gmail.com",
    "website": "",
    "license": "LGPL-3",
    "price": 16.66,
    "currency": "EUR",

    "depends": [
        "ma_pos_pin",
        "ma_pos_product_available",
    ],
    "external_dependencies": {"python": [], "bin": []},
    "data": [
        'data.xml',
        'views.xml',
    ],
    "demo": [
    ],
    "qweb": [
    ],

    'installable': True,
}
