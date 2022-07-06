import pandas as pd
import json, time
import numpy as np
import paho.mqtt.client as mqtt
from flask import Flask, request, render_template
from flask_restful import Resource, Api
import threading

class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        if isinstance(obj, np.floating):
            return float(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return super(NpEncoder, self).default(obj)


app = Flask(__name__)
api = Api(app)

class GeneratorThread:

    def __init__(self, protocol, freq, path, topic, address):
        self.protocol = protocol
        self.freq = freq
        self.path = path
        self.topic = topic
        self.address = address
        self.turn = 'on'
        thread = threading.Thread(target=self.generate, args=())
        thread.start()

    def mqtt_connector(self):

        self.client = mqtt.Client("data_sender")
        self.client.connect(self.address, 1883)
        self.client.subscribe(self.topic)

    def mqtt_sender(self,messamge):
        self.client.publish(self.topic, messamge)

    def data_from_file(self,path):
        return pd.DataFrame(pd.read_csv(path))

    def generate(self):
        data = self.data_from_file(self.path)
        index_numb = 0
        self.http_data = []
        self.mqtt_connector()
        while True:
            if self.turn == 'on':
                data = self.data_from_file(self.path)
                print(data)
                index_numb = 0
                self.http_data = []

            while self.turn == 'on':
                try:
                    data_to_send = dict(data.loc[index_numb])
                    data_to_send = json.dumps(data_to_send,cls=NpEncoder)
                    if self.protocol == 'http':
                        self.http_data.append(data_to_send)
                    elif self.protocol == 'mqtt':
                        self.mqtt_sender(data_to_send)

                    index_numb += 1
                    time.sleep(self.freq)
                except KeyError:
                    break


class DataChanger(Resource):

    def get(self):
        return gt.http_data

    def post(self): #we can handle only this 3 param
        new_settings = request.get_json(force=True)
        if new_settings['freq']:
            gt.frequency = new_settings['freq']
        if new_settings['turn']:
            gt.turn = new_settings['turn']
        if new_settings['mode']:
            gt.protocol = new_settings['mode']


class BasicInfo(Resource):
    global data_source

    def get(self):
        return f"{data_source} {gt.turn} {gt.protocol}"

# ustawienia początkowe
how_to_send = 'mqtt'
send_adress_http = 'http://127.0.0.1:5000/data/1'
send_adress_mqtt = "test.mosquitto.org"
mqtt_topic = "data_beach"
data_source = r'dane\IOT-temp.csv'
frequency = 5
status = 'off'


@app.route('/', methods=['GET', 'POST'])
def home():
    global how_to_send
    global data_source
    global frequency
    global status

    if request.method == 'POST':
        if request.form['frequency']:
            gt.frequency = request.form['frequency']
            frequency = request.form['frequency']
        if request.form['protocol']:
            gt.protocol = request.form['protocol']
            how_to_send = request.form['protocol']
        if request.form['turn']:
            gt.turn = request.form['turn']
            status = request.form['turn']
    return render_template('index.html', protocol = how_to_send, data = data_source,
                           frequency = str(frequency), name ='beach-water-quality', status = status)



api.add_resource(DataChanger, '/data', '/data')
api.add_resource(BasicInfo, '/info', '/info')


if __name__ == "__main__":
    gt = GeneratorThread(how_to_send, frequency, data_source, mqtt_topic, send_adress_mqtt)
    app.run(host='127.0.0.3')



