from flask import Flask
from flask_restful import Api
from . import looping_search

def app_mining():
    app = Flask(__name__)
    api = Api(app)

    api.add_resource(looping_search.LokalTerdaftar, '/pselokal/<int:a>/<int:b>')
    api.add_resource(looping_search.LokalDihentikan, '/pselokaln/<int:a>/<int:b>')
    api.add_resource(looping_search.AsingTerdaftar, '/pseasing/<int:a>/<int:b>')
    api.add_resource(looping_search.AsingDihentikan, '/pselokaln/<int:a>/<int:b>')

    return app   