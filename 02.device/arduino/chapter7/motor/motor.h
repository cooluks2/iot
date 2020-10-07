#pragma once

#include <Arduino.h>

class Motor {
protected:
    int in1;    // 전진
    int in2;    // 후진
    int en;     // 속도, PWM

public:
    Motor(int in1, int in2, int en);

    void forward(int speed=200);    // 전진
    void backward(int speed=200);   // 후진
    void stop();                    // 정지
    void setSpeed(int speed);
};