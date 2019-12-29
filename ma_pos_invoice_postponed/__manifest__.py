# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).
{
    "name": """Creation of Postponed invoices in POS""",
    "summary": """This module allows the usage of a regular POS order payment process to create an invoice to be paid later""",
    "category": "Point of Sale",
    "images": ['images/postponed2.jpg'],
    "version": "11.0.1.0.0",
    "application": False,
    "author": "Mediterranean Apps",
    "support": "mediterranean.apps@gmail.com",
    "website": "",
    "license": "LGPL-3",
    "price": 30.00,
    "currency": "EUR",

    "depends": [
        "point_of_sale",
    ],
    "external_dependencies": {"python": [], "bin": []},
    "data": [
        "views/views.xml",
        "views/assets.xml",
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

    # "demo_title": "Creation of Postponed invoices in POS",
    # "demo_addons": [
    # ],
    # "demo_addons_hidden": [
    # ],
    # "demo_url": "DEMO-URL",
    # "demo_summary": "This module allows the usage of a regular POS order payment process to create an invoice to be paid later",
    # "demo_images": [
    #    "images/MAIN_IMAGE",
    # ]
}
