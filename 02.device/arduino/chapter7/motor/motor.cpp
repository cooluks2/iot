#include "motor.h"

Motor::Motor(int in1, int in2, int en) : in1(in1), in2(in2), en(en) {
    pinMode(in1, OUTPUT);
    pinMode(in2, OUTPUT);
    pinMode(en, OUTPUT);
}

void Motor::forward(int speed) {    // 전진
    digitalWrite(in1, HIGH);
    digitalWrite(in2, LOW);
    analogWrite(en, speed);
}

void Motor::backward(int speed) {   // 후진
    digitalWrite(in1, LOW);
    digitalWrite(in2, HIGH);
    analogWrite(en, speed);
}

void Motor::stop() {                    // 정지
    digitalWrite(in1, LOW);
    digitalWrite(in2, LOW);
    analogWrite(en, 0);
}

void Motor::setSpeed(int speed) {
    analogWrite(en, speed);
}