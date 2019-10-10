"""."""
from flask_restful import Resource, reqparse
from elasticsearch import Elasticsearch
from modules.data_processing.helpers.text_cleaner import text_cleaner

parser = reqparse.RequestParser()
parser.add_argument('term', help='Rate to charge for this resource')

elastic = Elasticsearch()


class CurriculumController(Resource):
    """."""

    def get(self):
        """."""
        args = parser.parse_args()
        term = args['term']

        body = {
            '_source': {
                'excludes': ['corpus']
            },
            'from': 0,
            'query': {
                'bool': {
                    'must': [
                        {
                            'match_phrase': {
                                'corpus': text_cleaner.clean(term)
                            }
                        }
                    ]
                }
            }
        }
        return elastic.search(index="resumes", body=body)
    # if len(department) is not 0:
    #     s = {}
    #     s['bool'] = {}
    #     s['bool']['should'] = []
    #     body['query']['bool']['must'].append(s)
    #     for deps in department:
    #         d = { "match": { "department": deps } }
    #         body['query']['bool']['must'][1]['bool']['should'].append(d)
