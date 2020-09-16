#pragma once

#include <Arduino.h>

class Ultra {
protected:
    int echo;
    int trig;

public:
    Ultra(int echo, int trig);
    int read();

};