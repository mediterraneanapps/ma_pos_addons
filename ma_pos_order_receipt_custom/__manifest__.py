# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).
{
    "name": """Custom POS Kitchen Ticket""",
    "summary": """Customize POS kitchen ticket as you need""",
    "category": "Point of Sale",
    "images": ['images/pos_order_receipt_custom.jpg'],
    "version": "12.0.1.0.5",
    "application": False,

    "author": "Mediterranean Apps",
    "support": "mediterranean.apps@gmail.com",
   # "website": "",
    "license": "LGPL-3",
    "price": 6.66,
    "currency": "EUR",

    "depends": [
        "ma_pos_restaurant_base",
        "ma_pos_receipt_custom_template",
    ],
    "external_dependencies": {"python": [], "bin": []},
    "data": [
        "views/view.xml",
        "views/template.xml",
        "data/pos_order_receipt_custom_data.xml",
    ],
    "demo": [
    ],
    "qweb": [
    ],

    "post_load": None,
    "pre_init_hook": None,
    "post_init_hook": None,
    "uninstall_hook": None,

    "auto_install": False,
    "installable": True,
}
