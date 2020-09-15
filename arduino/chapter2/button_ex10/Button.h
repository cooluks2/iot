#pragma once

#include <Arduino.h>

class Button {
protected:
    int pin;
    bool state_previous = true;
    bool state_current;
    void (*callback)();

public:
    Button(int pin);
    int read();
    void setCallback(void (*callback)()); // 매개변수가 return 타입이 void인 함수의 대한 포인터 전달 받음.
    int check();
};