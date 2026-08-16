# IoT System with Raspberry Pi and MQTT

This project sets up a simple IoT system that uses a Raspberry Pi to read temperature and humidity data from a DHT11 sensor and sends the data to a server using MQTT protocol. The server then saves the data in a JSON file.

## How it works

There are two main components in this system: the sensor module and the server module.

The sensor module uses the Adafruit_DHT library to read data from a DHT11 sensor connected to a Raspberry Pi. The data is then sent to a MQTT broker running on localhost using the paho-mqtt library.

The server module uses the paho-mqtt library to connect to the MQTT broker and subscribe to the "home/sensor" topic. When it receives a message, it saves the data in a JSON file.

## How to run

1. Install the required libraries: `pip install paho-mqtt Adafruit_DHT`
2. Run the server: `python3 server.py`
3. In a separate terminal, run the sensor module: `python3 sensor.py`

## Example usage

After running the sensor and server modules, the server will start receiving temperature and humidity data from the sensor and save it in a `data.json` file.

## Notes on architecture and trade-offs

This system uses MQTT, which is a lightweight and efficient protocol designed for IoT devices. However, it assumes that the server and the sensor are running on the same machine. In a real-world scenario, they would likely be running on different machines, and you would need to set up a MQTT broker accessible over the internet.