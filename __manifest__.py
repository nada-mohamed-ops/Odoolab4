{
    'name': 'HMS',
    'version': '17.0.0.1.0',
    'category': 'Healthcare',
    'summary': 'Manage patients, departments, and doctors',
    'depends': ['base', 'web'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/menus.xml',
        'views/patient_view.xml',
        'views/department_view.xml',
        'views/doctor_view.xml',
        'wizards/log_history_wizard.xml',
    ],
    'installable': True,
}
