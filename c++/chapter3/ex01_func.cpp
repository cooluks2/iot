#include <iostream>
using namespace std;

int max(int x, int y);  // �Լ� ����

int main(int argc, char const *argv[]) {
    int n;
    n = max(2, 3);
    cout << "�Լ� ȣ�� ��� : " << n << endl;
    return 0;
}

int max(int x, int y) {
    if(x>y)
        return x;
    else
        return y;
}