#include <Servo.h>

Servo servoMotor;

const int servoMotorPin = 9;
int angle;

void setup() {
    servoMotor.attach(servoMotorPin);
    servoMotor.write(0);
    delay(1000);
}

void loop() {
    for (angle = 0; angle <= 179; angle++) {
        servoMotor.write(angle);
        delay(10);
    }
    delay(100);

    for (angle = 179; angle >= 0; angle--) {
        servoMotor.write(angle);
        delay(10);
    }
    delay(100);
}