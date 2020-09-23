#include <iostream>
using namespace std;

class Second {
public:
    int sec;

    Second() {
        sec = 0;
    }
    Second(int s) {
        sec = s;
    }
};

// Second second;  // 디폴트 생성자
// Second second(20);  // 매개변수 1개인 생성자

class Time {
public:
    int hour;
    int minute;
    Second sec;

    Time() : sec(20) {  //Second second(20); 과 같음
        hour = 0;
        minute = 0;
        // sec.second = 20;  // sec 인스턴스가 만들어진 이후에 하는 작업임.
    }

    Time(int h, int m) : hour(h), minute(m), sec(20) {  // int hour(h); int minute(m);
    }

    void print() {
        cout << hour << ":" << minute << endl;
    }
};

int main() {
    Time a;
    Time b(10, 25);

    a.print();
    b.print();

    return 0;
}