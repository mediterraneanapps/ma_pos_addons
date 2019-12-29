{
    "name": """Analyzing of refunds in Restaurant""",
    "summary": """Waiter specifies refund reason to avoid serving mistakes in future.""",
    "category": "Point of Sale",
    "images": ["images/pos_order_cancel_restaurant.png"],
    "version": "12.0.1.5.0",
    "application": False,

    "author": "Mediterranean Apps",
    "support": "mediterranean.apps@gmail.com",
    "website": "",
    "license": "LGPL-3",
    "price": 16.66,
    "currency": "EUR",

    "depends": [
        "ma_pos_order_cancel",
        "ma_pos_restaurant_base",
    ],
    "external_dependencies": {"python": [], "bin": []},
    "data": [
        "views/template.xml",
        "views/views.xml",
    ],
    'qweb': [
        'static/src/xml/cancel_order.xml',
    ],
    "demo": [
        'data/pos_cancelled_reason_demo.xml'
    ],

    "post_load": None,
    "pre_init_hook": None,
    "post_init_hook": None,

    "auto_install": False,
    "installable": True,
}
