import Adafruit_DHT
import time

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4

def log_temperature_and_humidity():
    with open('sensor_data.log', 'a') as f:
        while True:
            humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
            if humidity is not None and temperature is not None:
                f.write(f"Temp={temperature}*  Humidity={humidity}%\n")
            else:
                f.write("Failed to retrieve data from humidity sensor\n")

            time.sleep(3)

if __name__ == "__main__":
    log_temperature_and_humidity()