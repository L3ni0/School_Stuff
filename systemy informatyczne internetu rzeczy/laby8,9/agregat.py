import requests
import json
import numpy as np
import pandas as pd
from flask import Flask, request, render_template, Response
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

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



class Agregate(Resource):

    def post(self):
        info = request.get_json(force=True)
        print(info)
        r = requests.get("http://" + info["ip"] + "/data")
        data = r.json()
        data = list(map(json.loads, data))
        df = pd.DataFrame.from_dict(data)
        df['date'] = pd.to_datetime(df['date'])
        df = df.set_index('date')
        d1 = df.loc[info["from"]:info["to"]]
        to_return = dict(d1.mean().astype(int))
        to_return = json.dumps(to_return, cls=NpEncoder)
        return to_return

api.add_resource(Agregate, '/')

if __name__ == "__main__":
    app.run()
