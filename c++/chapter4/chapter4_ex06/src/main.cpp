#include <iostream>
#include <string>
#include "Car.hpp"
using namespace std;

int main(int argc, char const *argv[]) {
    Car myCar;

    myCar.setSpeed(100);

    cout << "�ӵ� : " << myCar.getSpeed() << endl;
    
    return 0;
}
