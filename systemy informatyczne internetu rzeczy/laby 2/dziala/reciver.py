import paho.mqtt.client as mqtt
import requests

mqttBroker = "test.mosquitto.org"


def on_message(client, userdata, message):
    data = message.payload.decode()
    print(data)
    requests.post('http://127.0.0.1:5000/data', data=data)


client = mqtt.Client("Subscriber")
client.connect(mqttBroker, 1883) 
client.subscribe("disc_usage")
client.on_message=on_message

client.loop_forever()
