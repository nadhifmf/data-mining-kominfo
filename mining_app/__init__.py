from flask import Flask
from flask_restful import Api
from . import looping_search

def app_mining():
    app = Flask(__name__)
    api = Api(app)

    api.add_resource(looping_search.LokalTerdaftar, '/pselokal/<int:a>/<int:b>')

    return app   