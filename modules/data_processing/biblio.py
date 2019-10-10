"""."""
import sys
import os
from lxml import etree
# import authorsFunc

DIR = os.path.dirname(__file__)
sys.path.insert(0, DIR + './helpers')


def get(curriculum):
    """."""
    data = {}
    data['articles'] = make(curriculum.xpath('//ARTIGO-PUBLICADO'), 'DADOS-BASICOS-DO-ARTIGO', 'DETALHAMENTO-DO-ARTIGO', 'AUTORES') if len(curriculum.xpath('//ARTIGO-PUBLICADO')) != 0 else False
    data['eventWorks'] = make(curriculum.xpath('//TRABALHO-EM-EVENTOS'), 'DADOS-BASICOS-DO-TRABALHO', 'DETALHAMENTO-DO-TRABALHO', 'AUTORES') if len(curriculum.xpath('//TRABALHO-EM-EVENTOS')) != 0 else False
    data['magazines'] = make(curriculum.xpath('//TEXTO-EM-JORNAL-OU-REVISTA'), 'DADOS-BASICOS-DO-TEXTO', 'DETALHAMENTO-DO-TEXTO', 'AUTORES') if len(curriculum.xpath('//TEXTO-EM-JORNAL-OU-REVISTA')) != 0 else False
    data['publishedOrganizedBooks'] = make(curriculum.xpath('//LIVRO-PUBLICADO-OU-ORGANIZADO'), 'DADOS-BASICOS-DO-LIVRO', 'DETALHAMENTO-DO-LIVRO', 'AUTORES') if len(curriculum.xpath('//LIVRO-PUBLICADO-OU-ORGANIZADO')) != 0 else False
    data['publishedChaptersBooks'] = make(curriculum.xpath('//CAPITULO-DE-LIVRO-PUBLICADO'), 'DADOS-BASICOS-DO-CAPITULO', 'DETALHAMENTO-DO-CAPITULO', 'AUTORES') if len(curriculum.xpath('//CAPITULO-DE-LIVRO-PUBLICADO')) != 0 else False

    return data


def make(dataSet, basicDataRef, detailsDataRef, authorsDataRef):
    """."""
    arr = []
    for data in dataSet:
        basic_data = data.xpath(basicDataRef)[0]
        details_data = data.xpath(detailsDataRef)[0]
        # authorsData = data.xpath(authorsDataRef)
        obj = {}
        obj['title'] = basic_data.get('TITULO-DO-ARTIGO') or basic_data.get('TITULO-DO-TRABALHO') or basic_data.get('TITULO-DO-LIVRO') or basic_data.get('TITULO-DO-CAPITULO-DO-LIVRO') or basic_data.get('TITULO-DO-TEXTO')
        year = basic_data.get('ANO') or basic_data.get('ANO-DO-ARTIGO') or basic_data.get('ANO-DO-TRABALHO')
        obj['year'] = int(year) if (year and len(year) == 4) else 0
        obj['nature'] = basic_data.get('NATUREZA')
        obj['country'] = basic_data.get('PAIS-DE-PUBLICACAO') or basic_data.get('PAIS-DO-EVENTO')
        obj['doi'] = basic_data.get('DOI')
        obj['language'] = basic_data.get('IDIOMA')
        if (details_data.get('TITULO-DO-PERIODICO-OU-REVISTA')):
            obj['magazine'] = {}
            obj['magazine']['magazineName'] = details_data.get('TITULO-DO-PERIODICO-OU-REVISTA')
            obj['magazine']['magazineVol'] = details_data.get('VOLUME')
            obj['magazine']['endAt'] = details_data.get('PAGINA-FINAL')
            obj['magazine']['startAt'] = details_data.get('PAGINA-INICIAL')
            obj['magazine']['issn'] = details_data.get('ISSN')
        if (details_data.get('NOME-DO-EVENTO')):
            obj['event'] = {}
            obj['event']['city'] = details_data.get('CIDADE-DO-EVENTO')
            obj['event']['name'] = details_data.get('NOME-DO-EVENTO')
            obj['event']['annalsTitle'] = details_data.get('TITULO-DOS-ANAIS-OU-PROCEEDINGS')
        # if (len(authorsData) is not 0):
        #     obj['authors'] = authorsFunc.get(authorsData)
        arr.append(obj)
    return sorted(arr, key=lambda x : (-x['year'], x['year']))
