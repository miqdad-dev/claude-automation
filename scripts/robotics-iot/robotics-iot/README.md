# Robotics/IoT - Light-controlled Servo

This project uses an arduino and a photoresistor to control the movement of a servo motor. The level of light detected by the photoresistor determines the angle of the servo motor.

## How It Works
The Arduino reads the value from the photoresistor using an analog input. It then maps this value to an angle for the servo motor (0 to 180 degrees). The more light the photoresistor detects, the greater the angle of the servo motor.

## How to Run

1. Connect the components as described in the circuit diagram (circuit.png).
2. Upload the Arduino code (servo_light_control.ino) to the Arduino.
3. Power on the Arduino.

## Example Usage
You can use a flashlight to control the servo. The brighter the light, the greater the servo's angle.

## Architecture & Tradeoffs
The code is simple and easy to understand, but it's not very robust. For example, it doesn't do any error checking. If the servo is not connected, the code will still run and won't give any error messages. I chose simplicity over robustness because this is a small, educational project.