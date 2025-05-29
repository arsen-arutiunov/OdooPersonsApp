{
    'name': 'Persons',
    'version': '16.0.1.0.0',
    'summary': 'Manage persons with backend and website views',
    'category': 'Website',
    'depends': ['base', 'website'],
    'data': [
        'security/ir.model.access.csv',
        'views/persons_views.xml',
        'views/templates.xml',
    ],
    'application': False,
    'installable': True,
}
