#include "Ultra.h"

Ultra::Ultra(int echo, int trig) : echo(echo), trig(trig) {
    pinMode(trig, OUTPUT);
    pinMode(echo, INPUT);
}

int Ultra::read() {
    // trigger 핀으로 10us의 펄스를 발생
    digitalWrite(trig, HIGH);
    delayMicroseconds(10);  // HIGH의 폭이 10㎲
    digitalWrite(trig, LOW);

    // echo 핀 입력으로부터 거리를 cm 단위로 계산
    int distance = pulseIn(echo, HIGH) / 58;

    return distance;
}