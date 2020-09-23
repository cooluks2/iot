#include <iostream>
#include <string>
using namespace std;

class Car{
public:
    int speed;    // 속도
    int gear;     // 기어
    string color; // 색상

    void speedUp() {
        speed += 10;
    }
    
    void speedDown(){
        speed -= 10;
    }
};

int main(int argc, char const *argv[])
{
    Car myCar;
    myCar.speed = 100;
    myCar.gear = 3;
    myCar.color = "red";

    myCar.speedUp();
    myCar.speedDown();

    return 0;
}