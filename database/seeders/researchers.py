import sys
import os
import csv

from main.models.Researchers import Researchers
from main.models.Departments import Departments

dir = os.path.dirname(__file__)

sys.path.insert(0, dir + '../../')

try:
    in_file = open('in.csv')
    csv_reader = csv.reader(in_file, delimiter=',')
    line_count = 0

    for row in csv_reader:
        code = row[1]
        cpf = ''.join(row[2].split('-'))
        cpf = ''.join(cpf.split(' '))
        try:
            d = Departments.get(Departments.code == code)
        except Departments.DoesNotExist as e:
            print(e)
            Departments.create(code=code, name=code)
            print('Departamento {} não encontrado'.format(
                code
            ))
            print('Departameto {}'.format(
                code
            ))
            d = Departments.get(Departments.code == code)
            pass

        Researchers.create(document=cpf, department=d)

except Exception as e:
    raise e
