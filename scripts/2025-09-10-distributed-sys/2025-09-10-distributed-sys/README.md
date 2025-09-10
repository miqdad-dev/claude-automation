# Distributed IoT System

This project is a distributed IoT system that uses MQTT (Message Queuing Telemetry Transport) protocol. The system simulates a sensor device that publishes temperature data to an MQTT broker, and a server that subscribes to the broker and logs the temperature data received.

## How It Works

1. The sensor device generates random temperature data and publishes it to an MQTT broker.
2. The server subscribes to the MQTT broker and logs the temperature data received.

## How to Run

1. Install the required Python packages: `pip install -r requirements.txt`
2. Run the sensor device: `python sensor.py`
3. Run the server: `python server.py`

## Example Usage

1. Run the sensor device: `python sensor.py`. You should see the temperature data being generated and published.
2. Run the server: `python server.py`. You should see the temperature data being logged.

## Notes on Architecture & Tradeoffs

The MQTT protocol is used for communication between the sensor device and the server. It is a lightweight and efficient protocol that is well-suited for IoT applications.

This system is a simple simulation and does not include any error handling or security features. In a real-world application, you would need to add error handling and security features (e.g., encryption, authentication).