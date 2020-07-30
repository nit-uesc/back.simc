"""."""
from database.migrations.migrations import call_migrations
from database.seeders.seeders import call_seeders
# import modules.data_processing.data_processing

import json

from flask import Flask, request
from flask_restful import Api
from flask_cors import CORS as cors
from flask_jwt_extended import JWTManager, jwt_required
from application.oauth.oauth import oauth
from application.controllers.CurriculumController import CurriculumController

# call_migrations()
# call_seeders()

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'jwt-secret-string'

cors(app)
api = Api(app)
jwt = JWTManager(app)


@app.route('/')
def index():
    """."""
    return 'Simc'


@app.route('/oauth/token', methods=['POST'])
def login():
    """Receive authorization."""
    try:
        auth = oauth(request.authorization)
    except Exception as e:
        return '{}'.format(e), 401

    try:
        return json.dumps(auth.validate())
    except Exception as e:
        return '{}'.format(e), 404


@app.route('/secret', methods=['GET'])
@jwt_required
def secret():
    """."""
    return 'dumb'


api.add_resource(CurriculumController, '/curriculum')


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
