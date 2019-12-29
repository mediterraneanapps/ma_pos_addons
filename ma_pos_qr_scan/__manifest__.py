{
    "name": """QR Code Scanning in POS""",
    "summary": """Scans QR codes via device's camera""",
    "category": "Point of Sale",
    "images": ["images/main.png"],
    "version": "12.0.1.0.1",
    "application": False,

    "author": "Mediterranean Apps",
    "support": "mediterranean.apps@gmail.com",
    "website": "",
    "license": "LGPL-3",
    "price": 6.66,
    "currency": "EUR",

    "depends": [
        "ma_pos_qr_payments",
    ],
    "external_dependencies": {"python": [], "bin": []},
    "data": [
        "views/assets.xml",
    ],
    "qweb": [
        "static/src/xml/templates.xml",
    ],

    "auto_install": False,
    "installable": True,
}
