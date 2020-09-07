#include <iostream>
using namespace std;

int max(int x, int y);  // 함수 원형

int main(int argc, char const *argv[]) {
    int n;
    n = max(2, 3);
    cout << "함수 호출 결과 : " << n << endl;
    return 0;
}

int max(int x, int y) {
    if(x>y)
        return x;
    else
        return y;
}