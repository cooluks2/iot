#include <iostream>  // �˻� ����: ����� lib -> �����Ϸ� lib
#include "Car.hpp"  // �˻� ����: cwd(& include �˻�) -> ����� lib -> �����Ϸ� lib

// Ŭ���� ���� ����
void Car::setSpeed(int s) {  // :: scope ������
    speed = s;
}

int Car::getSpeed() {
    return speed;
}