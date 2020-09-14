#pragma once

#include <Arduino.h>

class Button {
protected:
    int pin;
    bool state_previous;
    bool state_current;

public:
    Button(int pin);
    int read();
};