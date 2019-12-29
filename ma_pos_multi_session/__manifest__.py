# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).
{
    "name": """Sync POS orders""",
    "summary": """Use multiple POS for handling orders""",
    "category": "Point Of Sale",
    "images": ["images/pos-multi-session.png"],
    "version": "12.0.4.2.10",
    "application": False,

    "author": "Mediterranean Apps",
    "support": "mediterranean.apps@gmail.com",
    "website": "",
    "license": "LGPL-3",
    "price": 120.00,
    "currency": "EUR",

    "depends": [
        "ma_pos_multi_session_sync"
    ],
    "external_dependencies": {"python": [], "bin": []},
    "data": [
        "data/pos_multi_session_data.xml",
        "security/ir.model.access.csv",
        "views/pos_multi_session_views.xml",
        "multi_session_view.xml"
    ],
    "qweb": [
        "static/src/xml/pos_multi_session.xml",
    ],
    "demo": [
        "demo/demo.xml",
    ],

    "post_load": None,
    "pre_init_hook": None,
    "post_init_hook": None,

    "auto_install": False,
    "installable": True,

    "demo_title": "Sync POS orders across multiple sessions",
    "demo_addons": [
        "pos_disable_payment",
        "ma_pos_multi_session_sync",
        "ma_pos_multi_session_restaurant",
    ],
    "demo_addons_hidden": [
    ],
    "demo_url": "pos-multi-session",
    "demo_summary": "Use multiple POSes for handling orders",
    "demo_images": [
        "images/pos-multi-session.png",
    ]
}
