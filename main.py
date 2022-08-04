import requests
import json
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)
retur = []

class PrintJSon(Resource):
    def get(self, jumlah):
        for x in range(jumlah):
            Urla = "https://pse.kominfo.go.id/static/json-static/LOKAL_TERDAFTAR/"
            Urlb = ".json?page[page]=1&page[limit]=10&filter[search_term]="
            Url = Urla + str(x) + Urlb
            r = requests.get(Url)
            retur.append(r.json())
            print(retur)
        with open('pselokal.json', 'w') as json_file:
            json.dump(retur, json_file)
        return retur

api.add_resource(PrintJSon, '/pselokal/<int:jumlah>')

if __name__ == '__main__':
    app.run(debug=True)

