import pandas as pd
import json, time
import paho.mqtt.client as mqtt
from flask import Flask, request, render_template, Response
from flask_restful import Resource, Api
import threading
import requests


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

if __name__ == "__main__":
    app.run(debug=True)