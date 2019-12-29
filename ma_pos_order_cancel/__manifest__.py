# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).
{
    "name": """Saving removed products of POS order""",
    "summary": """Store all cases of product removing and allow to specify reasons for it""",
    "category": "Point of Sale",
    "images": ["images/pos_order_cancel.png"],
    "version": "12.0.1.3.0",
    "application": False,

    "author": "Mediterranean Apps",
    "support": "mediterranean.apps@gmail.com",
    "website": "",
    "license": "LGPL-3",
    "price": 66.66,
    "currency": "EUR",

    "depends": [
        "point_of_sale",
        "ma_pos_pin",
    ],
    "external_dependencies": {"python": [], "bin": []},
    "data": [
        "security/security.xml",
        "security/ir.model.access.csv",
        "views/template.xml",
        "views/views.xml",
        "views/pos_config_view.xml",
    ],
    'qweb': [
        'static/src/xml/cancel_order.xml',
    ],
    "demo": [
        'data/pos_cancelled_reason_demo.xml',
        'views/assets_demo.xml',
    ],

    "post_load": None,
    "pre_init_hook": None,
    "post_init_hook": None,

    "auto_install": False,
    "installable": True,
}
