{
    'name': 'Student Management',
    'author': 'Aspirex (Pvt) Ltd',
    'version': '18.0.0.1',
    'summary': 'Student Management',
    'description': """Student Management""",
    'website': 'aspirex.com',
    'depends': [
        'base'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/student_student_views.xml',
    ],
    'licence': 'LGPL-3',
    'installable': True,
    'application': False,
}