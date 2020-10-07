#include "motor.h"

Motor right(8, 7, 9);
Motor left(5, 4, 3);

void setup() {

}

void loop()
{
    // 전진
    left.forward();
    right.forward();
    delay(1000);

    // 정지
    left.stop();
    right.stop();
    delay(2000);

    // 후진
    left.backward();
    right.backward();
    delay(1000);

    // 정지
    left.stop();
    right.stop();
    delay(2000);
}