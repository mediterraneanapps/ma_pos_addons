# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).
{
    "name": """WeChat Payments in POS""",
    "summary": """Support WeChat QR-based payments (scan and show)""",
    "category": "Point of Sale",
    "images": ["images/main.jpg"],
    "version": "12.0.1.0.0",
    "application": False,

    "author": "Mediterranean Apps",
    "support": "mediterranean.apps@gmail.com",
    "website": "",
    "license": "LGPL-3",
    "price": 110.00,
    "currency": "EUR",

    "depends": [
        "ma_wechat",
        "ma_pos_qr_scan",
        "ma_pos_qr_show",
        "ma_pos_qr_payments",
        "ma_pos_longpolling",
    ],
    "external_dependencies": {"python": [], "bin": []},
    "data": [
        "views/assets.xml",
        "wizard/pos_payment_views.xml",
    ],
    "demo": [
    ],
    "qweb": [
        "static/src/xml/pos.xml",
    ],

    "auto_install": False,
    "installable": True,
}
