{
    'name': 'Student Management',
    'author': 'Aspirex (Pvt) Ltd',
    'version': '18.0.0.1',
    'summary': 'Student Management',
    'description': """Student Management""",
    'website': 'aspirex.com',
    'depends': [
        'base', 'mail',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/student_student_views.xml',
        'views/student_student_male_views.xml',
        'views/year_year_view.xml',
        'data/ir_sequence_data.xml',
        'views/student_tags_view.xml',
    ],
    'licence': 'LGPL-3',
    'installable': True,
    'application': False,
}