import pandas as pd
import json, requests, time
import paho.mqtt.client as mqtt


how_to_send = 'mqtt'
send_adress_http = 'http://127.0.0.1:5000/data/1'
send_adress_mqtt = "test.mosquitto.org"
mqtt_topic = "data_beach"
data_source = r'dane\beach-water-quality-automated-sensors-1.csv'
frequency = 5



data = pd.read_csv(data_source)
data = pd.DataFrame(data)
print(data.head())

if how_to_send == 'mqtt':
    client = mqtt.Client("data_sender")
    client.connect(send_adress_mqtt, 1883)
    client.subscribe(mqtt_topic)


index_numb = 0
while True:
    data_to_send = dict(data.loc[index_numb])
    data_to_send = json.dumps(data_to_send)
    if how_to_send == 'http':
        requests.post(send_adress_http, data = data_to_send)
        index_numb += 1
    elif how_to_send == 'mqtt':
        client.publish(mqtt_topic, data_to_send)
        index_numb += 1
    time.sleep(frequency)