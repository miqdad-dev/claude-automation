import paho.mqtt.client as mqtt
import json
import os

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("home/sensor")

def on_message(client, userdata, msg):
    data = json.loads(msg.payload)
    print(f'Received data: {data}')
    with open('data.json', 'a') as f:
        f.write(json.dumps(data) + '\n')

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1883, 60)

client.loop_forever()