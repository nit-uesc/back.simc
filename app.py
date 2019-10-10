"""."""
# import database.migrations.migrations
# import database.seeders.seeders
# import modules.data_processing.data_processing

from flask import Flask
from flask_restful import Api
from flask_cors import CORS as cors
from application.controllers.CurriculumController import CurriculumController
#
# call_migrations()
# call_seeders()

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'jwt-secret-string'

cors(app)
api = Api(app)


@app.route('/')
def index():
    """."""
    return 'Simc'


api.add_resource(CurriculumController, '/curriculum')


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
