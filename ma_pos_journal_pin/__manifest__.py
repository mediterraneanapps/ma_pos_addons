# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).
{
    "name": """POS Payments by Manager's PIN""",
    "summary": """Ask for manager permission before use the journal""",
    "category": "Point of Sale",
    "images": ['images/pos_journal_pin.jpg'],
    "version": "11.0.1.0.0",
    "application": False,

    "author": "Mediterranean Apps",
    "support": "mediterranean.apps@gmail.com",
    "website": "",
    "license": "LGPL-3",
    "price": 26.66,
    "currency": "EUR",

    "depends": [
        "ma_pos_pin",
    ],
    "external_dependencies": {"python": [], "bin": []},
    "data": [
        "views/assets.xml",
        "views/views.xml",
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

    # "demo_title": "Ask Manager to use journal",
    # "demo_addons": [
    # ],
    # "demo_addons_hidden": [
    # ],
    # "demo_url": "DEMO-URL",
    # "demo_summary": "Ask Manager to use journal",
    # "demo_images": [
    #    "images/MAIN_IMAGE",
    # ]
}
