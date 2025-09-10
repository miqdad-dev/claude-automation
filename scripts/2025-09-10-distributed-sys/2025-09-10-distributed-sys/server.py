import paho.mqtt.client as mqtt

# MQTT settings
BROKER = "mqtt.eclipse.org"
PORT = 1883
TOPIC = "Temperature"

# MQTT callback functions
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe(TOPIC)

def on_message(client, userdata, msg):
    print(f"{msg.topic} {msg.payload}")

# Create a MQTT client
client = mqtt.Client("Server")

# Assign MQTT callback functions
client.on_connect = on_connect
client.on_message = on_message

# Connect to MQTT broker
client.connect(BROKER, PORT)

# Start the MQTT client
client.loop_forever()