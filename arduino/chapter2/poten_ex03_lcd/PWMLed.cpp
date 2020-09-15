#include "PWMLed.h"

// : Led(pin), value(0) 없으면 에러 - 부모의 디폴트 생성자가 없기 때문에
PWMLed::PWMLed(int pin) : Led(pin), value(0) {  

}

int PWMLed::PWMLed getValue() {
    return value;
}
    
// 점점 밝아지는 것
void PWMLed::PWMLed fadeIn(int step) {
    value += step;
    if(value > 255) {
        value = 0;
    }
    analogWrite(pin, value);
}

// 점점 어두워지는 것
void PWMLed::PWMLed fadeOut(int step) {
    value -= step;
    if(value < 0) {
        value = 255;
    }
    analogWrite(pin, value);
}

void PWMLed::set(int value) {  // 오버라이드(Led.cpp 에서는 digitalWrite를 해줬음)
    analogWrite(pin, value);
}