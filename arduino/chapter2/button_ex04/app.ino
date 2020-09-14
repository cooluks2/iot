#include<SimpleTimer.h>

int pin_LED1 = 4;
int pin_LED2 = 3;
int pin_button = 11;
boolean LED_state = false;

SimpleTimer timer;

// 함수명 의미: 함수의 시작주소를 가지고 있는 포인터 상수다.
// 배열명의 의미 ? in a[10]; 변수 a 자체는 첫 번째 엘리먼트의 주소를 가리키는 포인터(상수)

void blink() {
    LED_state = !LED_state;
    digitalWrite(pin_LED1, LED_state);
}
void setup()
{
    pinMode(pin_LED1, OUTPUT);
    digitalWrite(pin_LED1, LED_state);
    pinMode(pin_LED2, OUTPUT);
    digitalWrite(pin_LED2, false);

    pinMode(pin_button, INPUT_PULLUP); // ☆☆☆☆☆☆
    timer.setInterval(1000, blink);  // 1초 간격으로 블링크
}
void loop()
{
    timer.run();  // 타이머 운영
    digitalWrite(pin_LED2, !digitalRead(pin_button));
}