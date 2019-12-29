# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).
{
    "name": """POS: rewards for shifts""",
    "summary": """Rewards for shifts in POS Debt & Credit notebook""",
    "category": "Point of Sale",
    "images": ['images/pos_debt_notebook_rewards.jpg'],
    "version": "12.0.1.0.0",
    "application": False,

    "author": "Mediterranean Apps",
    "support": "mediterranean.apps@gmail.com",
    "website": "",
    "license": "LGPL-3",
    "price": 3.00,
    "currency": "EUR",

    "depends": [
        "ma_pos_debt_notebook",
        "base_attendance",
        "barcodes",
    ],
    "external_dependencies": {"python": [], "bin": []},
    "data": [
        'security/pos_debt_notebook_reward_security.xml',
        'views/reward_view.xml',
        'views/reward_type_view.xml',
        'security/ir.model.access.csv',
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
