from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class WaterData(Resource):
    dane = []

    def get(self,id):
        return self.dane[id]

    def post(self,id):
        while len(self.dane) < id+1:
                self.dane.append([])
        print(self.dane, len(self.dane))
        self.dane[id].append(request.get_json(force=True))

@app.route('/', methods=['GET', 'POST'])
def home():
    return 'witaj w bazie danych "Beach Water Quality"'

api.add_resource(WaterData, '/data', '/data/<int:id>')


app.run()