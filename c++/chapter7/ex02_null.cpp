#include <iostream>
using namespace std;

void f(int i) {
    cout << "f(int)" << endl;
}

void f(char *p) {
    cout << "f(char *)" << endl;
}

int main() {
    int *pNumber = NULL;  // 권장
    int *pNumber2;  // 권장하지 않음, 임의의 초기값을 가짐

    if(pNumber != NULL) {  // 포인터 안정성 검사
        cout << *pNumber << endl;
    }

    if(pNumber2 != NULL) {  // 결과 장담 못함...
        cout << *pNumber2 << endl;
    }


    // f(NULL); -- int, char * 둘 다 가능하므로 에러
    f(nullptr);  // nullptr : 포인터 NULL의 의미하는 키워드
    return 0;
}