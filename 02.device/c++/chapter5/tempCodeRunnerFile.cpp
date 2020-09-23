#include <iostream>
using namespace std;

class Time {
public:
    int hour;
    int minute;
    // 생성자
    Time(int h, int m) {
        hour = h;
        minute = m;
    }

    void print() {
        cout << hour << ":" << minute << endl;
    }
};

int main() {
    // Time a;  // 디폴트 생성자 호출 - 에러
    Time b(10, 25);
    Time c{10, 25};
    Time d = {10, 25};

    b.print();
    c.print();
    d.print();

    return 0;
}