# License LGPL-3.0 (https://www.gnu.org/licenses/lgpl.html).
{
    'name': 'Find item by ref in POS',
    "summary": """Adds the ability to searching product by ref in POS""",
    "category": "Point Of Sale",
    "images": ['images/pos_scan_ref.jpg'],
    "version": "11.0.1.0.1",
    "application": False,

    "author": "Mediterranean Apps",
    "support": "mediterranean.apps@gmail.com",
    "website": "",
    "license": "LGPL-3",
    "price": 3.00,
    "currency": "EUR",

    "depends": ["point_of_sale"],
    "external_dependencies": {"python": [], "bin": []},
    "data": [
        "data.xml",
    ],
    "demo": [
    ],
    "qweb": [
    ],

    "post_load": None,
    "pre_init_hook": None,
    "post_init_hook": None,
    "uninstall_hook": None,

    'auto_install': False,
    'installable': True,

    # "demo_title": "{MODULE_NAME}",
    # "demo_addons": [
    # ],
    # "demo_addons_hidden": [
    # ],
    # "demo_url": "DEMO-URL",
    # "demo_summary": "{SHORT_DESCRIPTION_OF_THE_MODULE}",
    # "demo_images": [
    #    "images/MAIN_IMAGE",
    # ]
}
