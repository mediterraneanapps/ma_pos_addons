{
    'name': 'Product lot in POS',
    'version': '10.0.1.0.3',
    'author': 'Mediterranean Apps',
    'license': 'LGPL-3',
    'category': 'Point Of Sale',
    'website': '',
    'images': ['images/screenshot.png'],
    'price': 3.00,
    'currency': 'EUR',
    'depends': ['ma_product_lot', 'ma_pos_product_available'],
    'data': [
        'data.xml',
    ],
    'qweb': [
        'static/src/xml/pos.xml',
    ],
    'installable': True,
    'auto_install': False,
}
