#include <iostream>
using namespace std;

int main(int argc, char const *argv[]) {
    int list[]= {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int list2[10];

    // list2 = list;  // 문법 에러, = 연산자로 배열의 값이 복사되지 않음

    // 배열의 크기 계산 방법
    int length = sizeof(list) / sizeof(int);  // 40 / 4 => 10
    //     list의 메모리크기: int 크기(4) * 10개 --> 40byte
    cout << length;

    // 복사전 list2 출력
    for (auto i : list2) {
        cout << i << " ";
    }
    cout << endl;


    // list의 값을 list2로 복사 해보세요.
    for(int i=0; i<length; i++) {
        list2[i] = list[i];
    }


    // 복사된 list2를 출력하세요.
    for (auto i : list2) {
        cout << i << " ";
    }
    cout << endl;

    cout << list << endl;

    return 0;
}