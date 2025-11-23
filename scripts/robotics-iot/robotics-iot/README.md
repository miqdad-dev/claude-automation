# Robotics IOT

This is a simple project to control a two-wheeled robot using Raspberry Pi's GPIO.

## What it does

The robot can move forward, turn right, turn left and stop based on the commands received.

## How it works

The robot uses two motors to move. The states of the motors are controlled using Raspberry Pi's GPIO (General Purpose Input/Output). The motors can be in two states: HIGH (running) or LOW (stopped).

## How to run

1. Clone the repository.
2. Connect the motors to the GPIO pins of the Raspberry Pi.
3. Run the script using Python 3. Example: