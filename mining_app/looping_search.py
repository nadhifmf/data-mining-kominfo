import requests
import json
from flask_restful import Resource
from pathlib import Path

retur = []

class LokalTerdaftar(Resource):
    def get(self, a, b):
        for x in range(a-1, b-1):
            Urla = "https://pse.kominfo.go.id/static/json-static/LOKAL_TERDAFTAR/"
            Urlb = ".json?page[page]="
            Urlc = "&page[limit]=10&filter[search_term]="
            Url = Urla + str(x) + Urlb + str(x+1) + Urlc
            r = requests.get(Url)
            retur.append(r.json())
            print(retur)
        base = Path('JSONDump')
        dumpname = base / ('PSELokal' + str(a) + '-' + str(b) + '.json')
        base.mkdir(exist_ok=True)
        with open(dumpname, 'w') as json_file:
            json.dump(retur, json_file)
        return retur

class AsingTerdaftar(Resource):
    def get(self, a, b):
        for x in range(a-1, b):
            Urla = "https://pse.kominfo.go.id/static/json-static/ASING_TERDAFTAR/"
            Urlb = ".json?page[page]="
            Urlc = "&page[limit]=10&filter[search_term]="
            Url = Urla + str(x) + Urlb + str(x+1) + Urlc
            r = requests.get(Url)
            retur.append(r.json())
            print(retur)
        base = Path('JSONDump')
        dumpname = base / ('PSEAsing' + str(a) + '-' + str(b) + '.json')
        base.mkdir(exist_ok=True)
        with open(dumpname, 'w') as json_file:
            json.dump(retur, json_file)
        return retur