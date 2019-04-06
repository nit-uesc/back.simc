import sys
import os
dir = os.path.dirname(__file__)
sys.path.insert(0, dir + './helpers')

from lxml import etree
import authorsFunc

def get(curriculum):
    data = {}
    data['articles'] = make(curriculum.xpath('//ARTIGO-PUBLICADO'), 'DADOS-BASICOS-DO-ARTIGO', 'DETALHAMENTO-DO-ARTIGO', 'AUTORES') if len(curriculum.xpath('//ARTIGO-PUBLICADO')) is not 0 else False
    data['eventWorks'] = make(curriculum.xpath('//TRABALHO-EM-EVENTOS'), 'DADOS-BASICOS-DO-TRABALHO', 'DETALHAMENTO-DO-TRABALHO', 'AUTORES') if len(curriculum.xpath('//TRABALHO-EM-EVENTOS')) is not 0 else False
    data['magazines'] = make(curriculum.xpath('//TEXTO-EM-JORNAL-OU-REVISTA'), 'DADOS-BASICOS-DO-TEXTO', 'DETALHAMENTO-DO-TEXTO', 'AUTORES') if len(curriculum.xpath('//TEXTO-EM-JORNAL-OU-REVISTA')) is not 0 else False
    data['publishedOrganizedBooks'] = make(curriculum.xpath('//LIVRO-PUBLICADO-OU-ORGANIZADO'), 'DADOS-BASICOS-DO-LIVRO', 'DETALHAMENTO-DO-LIVRO', 'AUTORES') if len(curriculum.xpath('//LIVRO-PUBLICADO-OU-ORGANIZADO')) is not 0 else False
    data['publishedChaptersBooks'] = make(curriculum.xpath('//CAPITULO-DE-LIVRO-PUBLICADO'), 'DADOS-BASICOS-DO-CAPITULO', 'DETALHAMENTO-DO-CAPITULO', 'AUTORES') if len(curriculum.xpath('//CAPITULO-DE-LIVRO-PUBLICADO')) is not 0 else False

    return data
def make(dataSet, basicDataRef, detailsDataRef, authorsDataRef):
    arr = []
    for data in dataSet:
        basicData = data.xpath(basicDataRef)[0]
        detailsData = data.xpath(detailsDataRef)[0]
        authorsData = data.xpath(authorsDataRef)
        obj = {}
        obj['title'] = basicData.get('TITULO-DO-ARTIGO') or basicData.get('TITULO-DO-TRABALHO') or basicData.get('TITULO-DO-LIVRO') or basicData.get('TITULO-DO-CAPITULO-DO-LIVRO') or basicData.get('TITULO-DO-TEXTO')
        year = basicData.get('ANO') or basicData.get('ANO-DO-ARTIGO') or basicData.get('ANO-DO-TRABALHO')
        obj['year'] = int(year) if (year and len(year) is 4) else 0
        obj['nature'] = basicData.get('NATUREZA')
        obj['country'] = basicData.get('PAIS-DE-PUBLICACAO') or basicData.get('PAIS-DO-EVENTO')
        obj['doi'] = basicData.get('DOI')
        obj['language'] = basicData.get('IDIOMA')
        if (detailsData.get('TITULO-DO-PERIODICO-OU-REVISTA')):
            obj['magazine'] = {}
            obj['magazine']['magazineName'] = detailsData.get('TITULO-DO-PERIODICO-OU-REVISTA')
            obj['magazine']['magazineVol'] = detailsData.get('VOLUME')
            obj['magazine']['endAt'] = detailsData.get('PAGINA-FINAL')
            obj['magazine']['startAt'] = detailsData.get('PAGINA-INICIAL')
            obj['magazine']['issn'] = detailsData.get('ISSN')
        if (detailsData.get('NOME-DO-EVENTO')):
            obj['event'] = {}
            obj['event']['city'] = detailsData.get('CIDADE-DO-EVENTO')
            obj['event']['name'] = detailsData.get('NOME-DO-EVENTO')
            obj['event']['annalsTitle'] = detailsData.get('TITULO-DOS-ANAIS-OU-PROCEEDINGS')
        if (len(authorsData) is not 0):
            obj['authors'] = authorsFunc.get(authorsData)
        arr.append(obj)
    return sorted(arr, key=lambda x : (-x['year'], x['year']))
