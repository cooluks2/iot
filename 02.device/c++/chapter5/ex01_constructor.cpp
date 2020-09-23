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

void printTime(Time t) {  // call by value (reference: Time &t, address: Time *time)
    cout << "Time => " << t.hour << ":" << t.minute << endl;
}

int main() {
    // Time a;  // 디폴트 생성자 호출 - 에러
    Time b(10, 25);
    Time c{10, 25};
    Time d = {10, 25};

    // 정적 객체(할당)일 때 = 연산은 복사 입니다.
    c = b; // ? 복사인가 참조인가?
    c.hour = 3;

    b.print();
    c.print();
    d.print();

    printTime(b);
    printTime(c);
    printTime(d);

    return 0;
}