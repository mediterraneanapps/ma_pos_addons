# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).
{
    "name": """Customizable POS Receipt""",
    "summary": """Customize POS receipt view to your taste""",
    "category": "Point of Sale",
    "images": ["images/pos_receipt_custom_main.png"],
    "version": "12.0.1.0.2",
    "application": False,

    "author": "Mediterranean Apps",
    "support": "mediterranean.apps@gmail.com",
    "website": "",
    "license": "LGPL-3",
    "price": 16.33,
    "currency": "EUR",

    "depends": [
        "point_of_sale",
    ],
    "external_dependencies": {"python": [], "bin": []},
    "data": [
        "views/view.xml",
        "views/template.xml",
        "security/ir.model.access.csv",
        "data/data.xml",
    ],
    "demo": [
    ],
    "qweb": [
        "static/src/xml/pos.xml",
    ],

    "post_load": None,
    "pre_init_hook": None,
    "post_init_hook": None,
    "uninstall_hook": None,

    "auto_install": False,
    "installable": True,
}
