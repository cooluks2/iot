#pragma once

#include <Arduino.h>

class Led {  // Digital Device
protected:
    int pin;

public:
    Led(int pin);
    void on();
    void off();
    void toggle();
    void set(int value);
};