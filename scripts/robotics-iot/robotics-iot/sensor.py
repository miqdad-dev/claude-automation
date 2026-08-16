import paho.mqtt.client as mqtt
import Adafruit_DHT
import json
import time

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4

def read_sensor():
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    return humidity, temperature

client = mqtt.Client()

client.connect("localhost", 1883, 60)

while True:
    humidity, temperature = read_sensor()
    if humidity is not None and temperature is not None:
        data = {'temperature': temperature, 'humidity': humidity}
        client.publish("home/sensor", json.dumps(data))
    else:
        print("Failed to retrieve data from sensor")

    time.sleep(3)