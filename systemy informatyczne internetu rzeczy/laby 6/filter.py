import requests
import json
import numpy as np
import pandas as pd
from flask import Flask, request, render_template, Response
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Filter(Resource):

    def post(self):
        adress = ''
        to_filter = request.get_json(force=True)

        r = requests.get("http://" + to_filter["ip"] + "/data")
        del to_filter["ip"]
        data = r.json()
        data = list(map(json.loads, data))
        df = pd.DataFrame.from_dict(data)
        for name, value in to_filter.items():
            if name == 'adress':
                adress = "http://" + to_filter["adress"]
            else:
                df = df.loc[df[name] == value]
        to_return = df.to_json(orient='records')

        if adress:
            requests.post(adress, data=to_return)
            return f'data has been sended to {adress}'

        return to_return


class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (np.int_, np.intc, np.intp, np.int8,
                            np.int16, np.int32, np.int64, np.uint8,
                            np.uint16, np.uint32, np.uint64)):

            return int(obj)

        elif isinstance(obj, (np.float_, np.float16, np.float32, np.float64)):
            return float(obj)

        elif isinstance(obj, (np.complex_, np.complex64, np.complex128)):
            return {'real': obj.real, 'imag': obj.imag}

        elif isinstance(obj, (np.ndarray,)):
            return obj.tolist()

        elif isinstance(obj, (np.bool_)):
            return bool(obj)

        elif isinstance(obj, (np.void)):
            return None

api.add_resource(Filter, '/')

if __name__ == "__main__":
    app.run(host='127.0.0.3')
