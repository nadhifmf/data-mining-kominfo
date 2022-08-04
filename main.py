import requests
import json
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)
retur = []

class PrintJSon(Resource):
    def get(self):
        for x in range(909):
            Urla = "https://pse.kominfo.go.id/static/json-static/LOKAL_TERDAFTAR/"
            Urlb = ".json?page[page]=1&page[limit]=10&filter[search_term]="
            Url = Urla + str(x) + Urlb
            r = requests.get(Url)
            retur.append(r.json())
            print(retur)
        return retur

with open('pselokal.json', 'w') as json_file:
    json.dump(retur, json_file)

api.add_resource(PrintJSon, '/')

if __name__ == '__main__':
    app.run(debug=True)

