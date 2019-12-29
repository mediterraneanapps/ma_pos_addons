# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).
{
    "name": """Sync restaurant orders""",
    "summary": """Staff get order details immediately after waiter taps on tablet""",
    "category": "Point of Sale",
    "images": ['images/s2.png'],
    "version": "12.0.3.3.2",
    "application": False,

    "author": "Mediterranean Apps",
    "support": "mediterranean.apps@gmail.com",
    "website": "",
    "license": "LGPL-3",
    "price": 10.00,
    "currency": "EUR",

    "depends": [
        "ma_pos_restaurant_base",
        "ma_pos_multi_session",
    ],
    "external_dependencies": {"python": [], "bin": []},
    "data": [
        "views/views.xml",
    ],
    "qweb": [
    ],
    "demo": [
        "demo/demo.xml",
    ],

    "post_load": None,
    "pre_init_hook": None,
    "post_init_hook": None,

    "auto_install": True,
    "installable": True,
}
