import paho.mqtt.client as mqtt
import random
import time

# MQTT settings
BROKER = "mqtt.eclipse.org"
PORT = 1883
TOPIC = "Temperature"

# Create a MQTT client
client = mqtt.Client("Sensor")

# Connect to MQTT broker
client.connect(BROKER, PORT)

while True:
    # Generate random temperature data
    temperature = round(random.uniform(20.0, 30.0), 2)

    # Publish temperature data
    client.publish(TOPIC, temperature)

    # Sleep for 1 second
    time.sleep(1)