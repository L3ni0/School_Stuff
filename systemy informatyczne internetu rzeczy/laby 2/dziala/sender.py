import paho.mqtt.client as mqtt
import shutil
import time
import json

mqttBroker = "test.mosquitto.org"



client = mqtt.Client("Disc_usage")
client.connect(mqttBroker, 1883)

total, prev_used, old_free = shutil.disk_usage("/")

while True:
    total, used, free = shutil.disk_usage("/")
    times = time.time()
    if abs(used - prev_used) > 0:
        data = {}
        data[times] = used
        payload = json.dumps(data)
        client.publish("disc_usage", payload)
        print(f"opubliowano {used}, {times}")
        old_free = free
    time.sleep(1)