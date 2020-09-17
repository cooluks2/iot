#pragma once

#include <Arduino.h>

typedef void (*pulse_callback_t)(int);

class Pulse {
protected:
    int onDelay;    // HIGH 시간
    int offDelay;   // LOW 시간

    int value;      // 현재 상태값 (H/L)
    unsigned long oldTime;  // 최근 상태 변경 시점 기록
    bool state;     // 펄스의 운영 여부
    pulse_callback_t callback;

public:
    Pulse(int onDelay, int offDelay);

    void setDelay(int onDelay, int offDelay);
    void run();
    int read() { return value; }

    bool getState() { return state; }
    void play();
    void stop();

    void setCallback(pulse_callback_t callback) 
            {this->callback = callback;}
};