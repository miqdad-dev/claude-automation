import RPi.GPIO as GPIO
import time

class Robot:
    def __init__(self, left_motor, right_motor):
        self.left_motor = left_motor
        self.right_motor = right_motor
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.left_motor, GPIO.OUT)
        GPIO.setup(self.right_motor, GPIO.OUT)

    def forward(self, seconds):
        GPIO.output(self.left_motor, GPIO.HIGH)
        GPIO.output(self.right_motor, GPIO.HIGH)
        time.sleep(seconds)
        GPIO.output(self.left_motor, GPIO.LOW)
        GPIO.output(self.right_motor, GPIO.LOW)
        
    def turn_right(self, seconds):
        GPIO.output(self.left_motor, GPIO.HIGH)
        GPIO.output(self.right_motor, GPIO.LOW)
        time.sleep(seconds)
        GPIO.output(self.left_motor, GPIO.LOW)

    def turn_left(self, seconds):
        GPIO.output(self.left_motor, GPIO.LOW)
        GPIO.output(self.right_motor, GPIO.HIGH)
        time.sleep(seconds)
        GPIO.output(self.right_motor, GPIO.LOW)
        
    def stop(self):
        GPIO.output(self.left_motor, GPIO.LOW)
        GPIO.output(self.right_motor, GPIO.LOW)

    def cleanup(self):
        GPIO.cleanup()