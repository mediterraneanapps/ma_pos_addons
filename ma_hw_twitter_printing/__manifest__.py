{
    "name": """Print tweets with PosBox""",
    "summary": """Print tweets with specific hashtags""",
    "category": "Point of Sale",
    # "live_test_URL": "",
    "images": [],
    "version": "12.0.1.0.0",
    "application": False,

    "author": "Mediterranean Apps",
    "support": "mediterranean.apps@gmail.com",
   # "website": "",
    "license": "LGPL-3",
    # "price": 0.00,
    # "currency": "EUR",

    "depends": [
    ],
    "external_dependencies": {"python": ["twython", "escpos"], "bin": []},
    "data": [
    ],
    "qweb": [
    ],
    "demo": [
    ],

    "post_load": "post_load",
    "pre_init_hook": None,
    "post_init_hook": 'post_init',

    "auto_install": False,
    "installable": True,
}
