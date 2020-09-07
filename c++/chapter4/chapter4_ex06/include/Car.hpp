#include <string>
using namespace std;

// 클래스 원형
class Car {
// 디폴트 접근 제한자: private
    int speed;    // 속도
    int gear;     // 기어
    string color; // 색상

public:
    int getSpeed();  // 함수 원형
    void setSpeed(int s);
};