#include <iostream>
using namespace std;

int main(int argc, char const *argv[])
{
    int x, y;

    cout << "x���� �Է��ϼ��� ";
    cin >> x;

    cout << "y���� �Է��ϼ��� ";
    cin >> y;

    if (x > y)
        cout << "x�� y���� Ů�ϴ�." << endl;
    else
        cout << "y�� x���� ũ�ų� �����ϴ�." << endl;
    return 0;
}
