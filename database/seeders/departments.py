"""."""
from application.models.Departments import Departments


def call_departments_seeder():
    """."""
    departments = [
        {'code': 'DCAA', 'name': 'DEPARTAMENTO DE CIÊNCIAS AGRÁRIAS E AMBIENTAIS'},
        {'code': 'DCAC', 'name': 'DEPARTAMENTO DE CIÊNCIAS ADMINISTRAÇÃO E CONTÁBEIS'},
        {'code': 'DCB', 'name': 'DEPARTAMENTO DE CIÊNCIAS BIOLÓGICAS'},
        {'code': 'DCEC', 'name': 'DEPARTAMENTO DE CIÊNCIAS ECONÔMICAS'},
        {'code': 'DCET', 'name': 'DEPARTAMENTO DE CIÊNCIAS EXATAS E TECNOLÓGICAS'},
        {'code': 'DCIE', 'name': 'DEPARTAMENTO DE CIÊNCIAS DA EDUCAÇÃO'},
        {'code': 'DCIJUR', 'name': 'DEPARTAMENTO DE CIÊNCIAS JURÍDICAS'},
        {'code': 'DCS', 'name': 'DEPARTAMENTO DE CIÊNCIAS DA SAÚDE'},
        {'code': 'DFCH', 'name': 'DEPARTAMENTO DE FILOSOFIA E CIÊNCIAS HUMANAS'},
        {'code': 'DLA', 'name': 'DEPARTAMENTO DE LETRAS E ARTES'},
        {'code': 'HV', 'name': 'HOSPITAL VETERINÁRIO'},
        {'code': 'REITORIA', 'name': 'REITORIA'},
        {'code': 'VICE REITORIA', 'name': 'VICE REITORIA'},
        {'code': 'OUVIDORIA', 'name': 'OUVIDORIA'}
    ]

    Departments.insert_many(departments).execute()
