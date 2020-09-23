#pragma once

#include <Arduino.h>
#include <Led.h>

class PWMLed : public Led {  // pin,on(),off(),set()는 Led.h에 있어서 상속받는다.
protected:
    int value;

public:
    PWMLed(int pin);
    
    int getValue();
    void fadeIn(int step=1);  // 점점 밝아지는 것
    void fadeOut(int step=1); // 점점 어두워지는 것
    void set(int value);
};