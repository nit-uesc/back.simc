"""."""
import pandas as pd
import multiprocessing as mp
import os
from elasticsearch import Elasticsearch, helpers
from peewee import DoesNotExist

from modules.data_processing.models.Curriculum import Curriculum
from modules.data_processing.helpers.json import json

from application.models.Researchers import Researchers
from application.models.Departments import Departments

elastic = Elasticsearch()


def generate_code(department):
    """."""
    parts = department.split()

    code = ''
    for part in parts:
        code += part[0]
    return code


def process_database(department, document):
    """."""
    try:
        department = Departments.get(Departments.code == department)
    except Departments.DoesNotExist as e:
        print('Departamento {} não encontrado. \n{}'.format(department, e))
        Departments.create(code=generate_code(department), name=department)
        department = Departments.get(Departments.code == generate_code(department))
        pass

    return Researchers.create(document=document, department=department)


def process_json(researcher):
    """."""
    document = researcher.document
    # file_name = document + '.xml'
    curriculum = Curriculum(researcher)
    summary = curriculum.get_summary()
    json.save('public/summary/' + document + '.json', summary)
    return process_elastic(curriculum)

    # this one is going to be pushed to elasticsearch
    # bag_of_words = curriculum.get_text()
    # json.save('public/corpus/' + code + '.json', bag_of_words)
    # db.query('UPDATE pesquisador_meta SET extraido = 1 WHERE id = '{}''.format(identificador))
    # db.commit()
    #
    # tamanho_do_arquivo = curriculo.stat.st_size//1024
    # stat.insert((tamanho_do_arquivo, tempo_de_execucao))
    # stat.save_csv()
    #
    # dictionary.append(curriculo.dictionary)
    # global_dictionary = join_dicts(global_dictionary, curriculo.dictionary)
    #


def process_elastic(curriculum):
    """."""
    summary = curriculum.get_summary()
    data = {
        '_index': 'resumes',
        '_type': 'resume',
        '_id': curriculum.get_document(),
        '_source': {
            'code': curriculum.get_document(),
            'name': summary['name'],
            'rank': summary['rank'],
            'department': summary['departament'],
            'abstract': summary['abstract'] if 'abstract' in summary else '',
            'graduation': summary['graduacao'],
            'masters': summary['mestrado'],
            'phd': summary['doutorado'],
            'posPhd': summary['pos-doutorado'],
        }
    }
    data["_source"]["corpus"] = curriculum.get_text()
    return data


def process_frame(researchers):
    """."""
    BULK = []
    for index, row in researchers.iterrows():
        department = row['department']
        document = ''.join(''.join(row['document'].split('-')).split(' '))
        try:
            researcher = Researchers.get(Researchers.document == document)
            # here I should collect and update
        except DoesNotExist:
            researcher = process_database(department, document)
        file_name = researcher.document + '.xml'
        if os.path.isfile('public/xml/' + file_name):
            BULK.append(process_json(researcher))
        else:
            print(file_name)
    return BULK


def process():
    """."""
    csv = pd.read_csv('in.csv', delimiter=',', chunksize=100)
    pool = mp.Pool(4)

    funclist = []
    for df in csv:
        f = pool.apply_async(process_frame, [df])
        funclist.append(f)
    BULK = []
    for f in funclist:
        BULK += f.get(timeout=100)

    helpers.bulk(elastic, BULK)
    print('There are {} rows of data'.format(len(BULK)))


process()
