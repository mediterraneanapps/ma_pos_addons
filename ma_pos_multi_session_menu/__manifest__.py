{
    "name": """Product Sets for POS (multisession extension)""",
    "summary": """Synchronize product sets across several POSes""",
    "category": "Point of Sale",
    "images": ["images/pos_multi_session_menu_main.jpg"],
    "version": "11.0.1.0.0",
    "application": False,

    "author": "Mediterranean Apps",
    "support": "mediterranean.apps@gmail.com",
   # "website": "",
    "license": "LGPL-3",
    "price": 9.66,
    "currency": "EUR",

    "depends": [
        "ma_pos_multi_session",
        "ma_pos_menu",
    ],
    "external_dependencies": {"python": [], "bin": []},
    "data": [
        "views/pos_menu_view.xml",
        "views/pos_multi_session_menu_template.xml",
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
}
