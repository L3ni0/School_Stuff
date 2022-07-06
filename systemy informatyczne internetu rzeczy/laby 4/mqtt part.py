import paho.mqtt.client as mqtt


mqttBroker = "test.mosquitto.org"


def on_message(client, userdata, message):
    data = message.payload.decode()
    print(data)



client = mqtt.Client("data_reciver")
client.connect(mqttBroker, 1883)
client.subscribe("data_beach")
client.on_message=on_message

client.loop_forever()