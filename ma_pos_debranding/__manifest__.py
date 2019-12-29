{
    'name': "POS debranding",
    'version': '12.0.1.0.0',
    'author': 'Mediterranean Apps',
    'license': 'LGPL-3',
    'category': 'Debranding',
    "support": "mediterranean.apps@gmail.com",
    'website': '',
    'depends': ['point_of_sale'],
    'price': 3.33,
    'currency': 'EUR',
    'data': [
        'views.xml',
        'template.xml'
    ],
    'qweb': [
        'static/src/xml/pos_debranding.xml',
    ],
    'installable': True,
}
