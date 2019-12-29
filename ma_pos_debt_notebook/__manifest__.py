# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

{
    'name': 'POS Debt & Credit notebook',
    'summary': 'Comfortable sales for your regular customers. Debt payment method for POS',
    'category': 'Point Of Sale',
    "images": ['images/debt_notebook.png'],
    'version': '12.0.5.3.2',
    'author': 'Mediterranean Apps',
    "support": "mediterranean.apps@gmail.com",
    'website': '',
    'license': 'LGPL-3',
    "price": 93.33,
    "currency": "EUR",

    "external_dependencies": {"python": [], "bin": []},
    'depends': [
        'point_of_sale',
    ],
    'data': [
        'security/pos_debt_notebook_security.xml',
        'data/product.xml',
        'views/pos_debt_report_view.xml',
        'views.xml',
        'views/pos_credit_update.xml',
        'wizard/pos_credit_invoices_views.xml',
        'wizard/pos_credit_company_invoices_views.xml',
        'data.xml',
        'security/ir.model.access.csv',
    ],
    'qweb': [
        'static/src/xml/pos.xml',
    ],
    "demo": [
        'data/demo.xml',
    ],
    'installable': True,
    'uninstall_hook': 'pre_uninstall',

    "demo_title": "POS Debt/Credit Notebook",
    "demo_addons": [
    ],
    "demo_addons_hidden": [
    ],
    "demo_url": "pos-debt-notebook",
    "demo_summary": "Comfortable sales for your regular customers.",
    "demo_images": [
        "images/debt_notebook.png",
    ]
}
