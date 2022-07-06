import base64
from PIL import Image
import pandas as pd
import json, time
import paho.mqtt.client as mqtt
from flask import Flask, request, render_template, Response
import jsonify
from flask_restful import Resource, Api
import threading
import requests
import io
import numpy as np


app = Flask(__name__)
api = Api(app)


machines_data = {}
to_send_data = {}


@app.route('/',methods=['GET', 'POST'])
def home():
    global machines_data, to_send_data

    if request.method == 'POST':

            r = requests.get(request.form['path']+'/info')

            name, status, protocol =  r.text.split(' ')
            machines_data[name[7:]] = [status, protocol.strip()]
            to_send_data[request.form['path']] = [name[7:], status, protocol.strip()]

    print(machines_data)
    return render_template("zazrzadca.html", datas=machines_data)


@app.route('/s/<ip>', methods=['GET', 'POST'])
def setings(ip):

    data = to_send_data['http://'+ip]
    if request.method == 'POST':
        send_setting = {'freq' : int(request.form['frequency']),
                        'turn' : f'{request.form["turn"]}',
                        'mode' : f'{request.form["protocol"]}'}
        send_setting = json.dumps(send_setting)

        machines_data[data[0]] = [request.form["turn"], request.form["protocol"]]
        to_send_data['http://' + ip] = [data[0],request.form["turn"], request.form["protocol"]]

        requests.post('http://'+ip+'/data', data=send_setting)


    return render_template("index.html", name = data[0], protocol = data[2], status= data[1])


@app.route('/a/<ip>', methods=['GET', 'POST'])
def agregat(ip):
    if request.method == 'POST':
        send_info = {'ip': ip+':5000',
                     'from': request.form["from"],
                     'to': request.form["to"]}
        print(send_info)
        send_info = json.dumps(send_info)
        r = requests.post('http://127.0.0.1:5000/' ,data=send_info)
        to_return = r.json()
        return to_return

    return render_template("agregat.html")


@app.route('/f/<ip>', methods=['GET', 'POST'])
def filter(ip):
    if request.method == 'POST':
        send_info = {'ip': ip+':5000',
                     request.form["from"]: request.form["to"],
                     'adress': request.form["adres"]}
        print(send_info)
        data = json.dumps(send_info)
        r = requests.post('http://127.0.0.3/', data=send_info)
        return r.json()

    return render_template("filter.html")


@app.route('/g/<ip>', methods=['GET', 'POST'])
def wiz(ip):
    if request.method == 'POST':
        send_info = {'ip': ip+':5000',
                     'x': request.form["x"],
                     'y': request.form["y"]}
        send_info = json.dumps(send_info)
        r = requests.post('http://127.0.0.5:5000/', data=send_info)
        to_return = r.json()
        image = json.loads(to_return)
        image = base64.b64decode(image)
        image = io.BytesIO(image)
        image = Image.open(image)
        image.save('obrazy\cos.jpg')


        return render_template('obraz.html')

    return render_template('wizualize.html')

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

if __name__ == "__main__":
    app.run(host='127.0.0.2')