{
    'name': 'Custom Tailwind',
    'version': '1.0',
    'summary': 'Custom Tailwind Css for Odoo Framework',
    'description': 'Web Design Development',
    'category': 'Uncategorized',
    'author': '-',
    'depends': [],
    'data': [],
    'qweb': [],  # Jika ada QWeb template tambahan, masukkan di sini
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
    'assets': {
        'web.assets_frontend': [
            'custom_tailwind/static/src/css/dist/output.css',
        ],
    },
}
