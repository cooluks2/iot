#include <iostream>
#include <string>
#include "Car.hpp"
#include "PrintData.hpp"
using namespace std;

int main(int argc, char const *argv[]) {
    Car myCar;

    myCar.setSpeed(100);

    cout << "speed : " << myCar.getSpeed() << endl;
    

    PrintData pd;
    pd.print(10);
    pd.print(10.2);
    pd.print("Hello World!");

    return 0;
}

