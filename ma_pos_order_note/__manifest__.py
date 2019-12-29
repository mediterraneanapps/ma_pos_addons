{
    "name": """POS Advanced Order Notes""",
    "summary": """Set predefined notes for separate product or entire order""",
    "category": "Point of Sale",
    "images": ["images/pos_order_note_main.png"],
    "version": "12.0.1.3.2",
    "application": False,

    "author": "Mediterranean Apps",
    "support": "mediterranean.apps@gmail.com",
    "website": "",
    "license": "LGPL-3",
    "price": 11.33,
    "currency": "EUR",

    "depends": [
        "ma_pos_restaurant_base",
    ],
    "external_dependencies": {"python": [], "bin": []},
    "data": [
        "security/ir.model.access.csv",
        "views/views.xml",
        "views/template.xml",
    ],
    "qweb": [
        "static/src/xml/order_note.xml",
    ],
    "demo": [
        "data/pos_product_notes_demo.xml",
    ],

    "post_load": None,
    "pre_init_hook": None,
    "post_init_hook": None,

    "auto_install": False,
    "installable": True,

    "demo_title": "POS Advanced Order Notes",
    "demo_addons": [
    ],
    "demo_addons_hidden": [
    ],
    "demo_url": "pos-order-note",
    "demo_summary": "Set predefined notes for separate product or entire order",
    "demo_images": [
        "images/pos_order_note_main.png",
    ]
}
