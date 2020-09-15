#include "Led.h"
#include "Button.h"

Led led(4);
Button btn(10);

void setup() {
    Serial.begin(9600);
    btn.setCallback(work);
}

void work() {
    led.toggle();
}

void loop()
{
    // led.set(btn.read());
    btn.check(); // 에지(Falling)가 발생했는지 체크
    // workPtr = work; // 매개변수가 없고 리턴타입이 void인 함수
}

// 함수 포인터 형식: void (*포인트_변수명)(매개변수);