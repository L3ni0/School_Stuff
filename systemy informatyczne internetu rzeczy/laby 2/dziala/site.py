from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

dane = []

@app.route('/', methods=['GET', 'POST'])
def home():
    return 'start site'


class DiscData(Resource):
    def get(self):
        return dane
    def post(self):
        dane.append(request.get_json(force=True))


api.add_resource(DiscData, '/data')


app.run()