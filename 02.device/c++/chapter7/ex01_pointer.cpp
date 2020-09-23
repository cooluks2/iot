#include <iostream>
using namespace std;
int main() {
    int number = 0;
    double d = 20.2;

    int *p = &number;
    // p = &d;  // 에러
    double *pd = &d;

    cout << p << endl;
    cout << *p << endl;

    cout << sizeof(number) << "," << sizeof(d) << endl;
    cout << sizeof(p) << endl;  // int *
    cout << sizeof(pd) << endl;  // double *

    return 0;
}
