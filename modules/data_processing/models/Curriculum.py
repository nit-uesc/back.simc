"""."""
# import os
import collections
from lxml import etree
from xmljson import badgerfish as bf
from modules.data_processing.helpers.text_cleaner import text_cleaner

from modules.data_processing.helpers.tags import tags


class Curriculum():
    """."""

    def __init__(self, researcher):
        """."""
        self.__document = researcher.document
        self.__tree = etree.parse('public/xml/' + researcher.document + '.xml')
        self.summary = self.make_summary(researcher)
        self.text = self.make_text()
        # self.stat = os.stat(dir + '/../curriculos_xml/' + document + '.xml')
        self.dict = {}

    def get_document(self):
        """."""
        return self.__document

    def get_tree(self):
        """."""
        return self.__tree

    def get_text(self):
        """."""
        return self.text

    def get_summary(self):
        """."""
        return self.summary

    def make_text(self):
        """."""
        document = u''

        for tag in tags:
            for xml_element in self.__tree.xpath(tag):
                attrs = tags[tag]
                document += xml_element.text or ''
                document += " "
                for attr in attrs:
                    document += xml_element.get(attr) or ''
                    document += " "

        document = text_cleaner.remove_special_characters(document)

        document = text_cleaner.remove_accents(document)

        document = u" ".join([w for w in document.split(' ') if w.isalpha()])

        document = document.lower()

        # return document

        stem = text_cleaner.stem(document)

        self.dictionary = stem['dictionary']
        document = stem['stemmed_text']

        return document

    def make_summary(self, researcher):
        """."""
        data = collections.OrderedDict()
        data['document'] = self.__document
        data['departament'] = researcher.department.code
        data['rank'] = ''

        # data['departament'] = PesquisadorMetaModel.getDepartamento(self.__identificador)

        for abstract in self.__tree.xpath('//DADOS-GERAIS'):
            data['name'] = abstract.get('NOME-COMPLETO') or ''
            data['country'] = abstract.get('PAIS-DE-NASCIMENTO') or ''

        for abstract in self.__tree.xpath('//RESUMO-CV'):
            data['abstract'] = abstract.get('TEXTO-RESUMO-CV-RH') or ''
        #
        levels = ['GRADUACAO', 'MESTRADO', 'DOUTORADO', 'POS-DOUTORADO']
        for level in levels:
            data[level.lower()] = []
            for abstract in self.__tree.xpath('//' + level):
                fields = []
                knowledge_fields = abstract.find('AREAS-DO-CONHECIMENTO')
                if knowledge_fields is not None:
                    for field in knowledge_fields:
                        fields.append((field.get('NOME-GRANDE-AREA-DO-CONHECIMENTO') or '', field.get('NOME-DA-SUB-AREA-DO-CONHECIMENTO') or '', field.get('NOME-DA-ESPECIALIDADE') or '',))
                data[level.lower()].append((abstract.get('NOME-CURSO') or '', abstract.get('NOME-INSTITUICAO') or '', abstract.get('ANO-DE-CONCLUSAO') or '', abstract.get('TITULO-DA-DISSERTACAO-TESE') or '', fields))
        #
        levels = ['GRADUACAO', 'MESTRADO', 'DOUTORADO']
        for level in levels:
            if len(data[level.lower()]) > 0:
                data['rank'] = [level.capitalize()] + list(data[level.lower()][0])

        return data

    def to_json(self):
        """."""
        return bf.data(self.__tree.getroot())
