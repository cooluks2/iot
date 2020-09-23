#include "Pulse.h"

Pulse::Pulse(int onDelay, int offDelay)
    : onDelay(onDelay), offDelay(offDelay) {

    value = HIGH;
    state = false;  // 시작은 운영 안함
    callback = NULL;
    oldTime = millis();
}


void Pulse::setDelay(int onDelay, int offDelay) {
    this->onDelay = onDelay;
    this->offDelay = offDelay;
}

void Pulse::play() {
    state = true;
    value = HIGH;
    oldTime = millis();
}

void Pulse::stop() {
    state = false;
    value = LOW;
}

void Pulse::run() {
    if(!state) return;

    unsigned long currentTime = millis();
    unsigned long diff = currentTime - oldTime;
    long interval = value ? onDelay : offDelay;

    if(diff >= interval) {
        oldTime = currentTime;
        value = !value;
        if(callback!=NULL) {
            callback(value);
        }
    }
}