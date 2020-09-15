#include "Button.h"

Button::Button(int pin) : pin(pin){
    pinMode(pin, INPUT_PULLUP);
    state_previous = true; // 디폴트 상태가 HIGH.
    callback = NULL;
}

int Button::read() {
    return !digitalRead(pin); // 풀업이라 반전
    // 실제 하드웨어는 pullup, 소프트웨어에선 pulldown형식으로 운영하기 위해 반전
}

void Button::setCallback(void (*callback)()) {
    this->callback = callback;
}

int Button::check() {
    state_current = digitalRead(pin);
    if(!state_current) { //누른경우
        if(state_previous == true) {
            state_previous = false;
            //버튼을 누른 시점에서 해야할 작업
            // work();  // timer.setInterval(100, work); // work: 함수에 대한 포인터
            if (callback != NULL) {
                callback();
            }
        }
        delay(5);
    } else {
        state_previous = true;
    }
}
