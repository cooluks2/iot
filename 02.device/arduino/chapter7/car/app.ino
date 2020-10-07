#include <car.h>

Car car(8, 7, 9, 5, 4 ,3);

void setup() {

}

void loop()
{
    // 전진
    car.forward();
    delay(2000);

    // 정지
    car.stop();
    delay(2000);

    // 후진
    car.backward();
    delay(1000);

    // 정지
    car.stop();
    delay(2000);

    car.turnLeft();
    delay(500);

    car.stop();
    delay(1000);

    car.turnRight();
    delay(500);

    car.stop();
    delay(1000);
}