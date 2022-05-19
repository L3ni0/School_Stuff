import io

import matplotlib.figure
from PIL import Image
import requests
import json
import numpy as np
import pandas as pd
import plotly
import plotly.express as px
import matplotlib.pyplot as plt
import jsonify
import base64
from flask import Flask, request, render_template, Response, send_file
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Wizualize(Resource):
    """
    class get 3 params
    ip : ip of data resource
    x : name of data what be on x axis
    y : name y axis data
    """
    def post(self):
        info = request.get_json(force=True)

        r = requests.get("http://" + info["ip"] + "/data")
        data = r.json()
        data = list(map(json.loads, data))
        df = pd.DataFrame.from_dict(data)

        x = info['x']

        plt.Figure()
        plt.hist(x)
        plt.title(info['x'])
        buf = io.BytesIO()
        plt.savefig(buf, format='JPEG')
        buf.seek(0)
        im = Image.open(buf)
        img_byte = base64.b64encode(buf.getvalue())
        img_str = img_byte.decode('utf_8')
        print(img_str)
        return json.dumps(img_str)


api.add_resource(Wizualize, '/')

if __name__ == "__main__":
    app.run(host='127.0.0.5')