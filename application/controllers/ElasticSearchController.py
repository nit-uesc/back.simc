"""."""
from flask_restful import Resource, reqparse
parser = reqparse.RequestParser()


class ElasticSearchController(Resource):
    """."""

    def get(self):
        """."""
