#include <iostream>
using namespace std;

int main(int argc, char const *argv[]) {
    int x = 100;

    if(x == 100)
        cout << "x�� 100�Դϴ�." << endl;

    if(x == 100) {
        cout << "x�� ���� ����մϴ�." << endl;
        cout << "x�� 100�Դϴ�." << endl;
    }

    return 0;
}
