#include <ArduinoUnit.h>
#include "servo_light_control.ino"

test(photoresistor_value) {
  // Simulate a mid-range light level.
  analogWrite(photoresistor, 512);
  loop();
  assertEqual(myservo.read(), 90);
}

test(photoresistor_value_low) {
  // Simulate a low light level.
  analogWrite(photoresistor, 0);
  loop();
  assertEqual(myservo.read(), 0);
}

test(photoresistor_value_high) {
  // Simulate a high light level.
  analogWrite(photoresistor, 1023);
  loop();
  assertEqual(myservo.read(), 180);
}

void setup() {
  Serial.begin(9600);
  TestRunner::setPrinter(Serial);
  myservo.attach(9);
  pinMode(photoresistor, OUTPUT);
}

void loop() {
  TestRunner::run();
  delay(100);
}