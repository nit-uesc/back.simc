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
        try:
            d = Departments.get(Departments.code == code)
        except Departments.DoesNotExist as e:
            Departments.create(code=code, name=code)
            print('Departamento {} não encontrado'.format(
                code
            ), e)
            print('Departameto {}'.format(
                code
            ))
            pass

except Exception as e:
    raise e
