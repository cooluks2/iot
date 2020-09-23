#include <iostream>
using namespace std;

int main(int argc, char const *argv[]) {
    int x = 100;

    if(x == 100)
        cout << "x가 100입니다." << endl;

    if(x == 100) {
        cout << "x의 값을 출력합니다." << endl;
        cout << "x가 100입니다." << endl;
    }

    return 0;
}
