#include <iostream>
#include <string>
using namespace std;
int main(int argc, char const *argv[])
{
    string s1, addr;
    cout << "�̸��� �Է��ϼ���: ";
    cin >> s1;
    cin.ignore(); // ����Ű ����

    cout << "�ּҸ� �Է��ϼ���: ";
    getline(cin, addr);
    
    cout << addr << "��" << s1 << "�� �ȳ��ϼ���?" << endl;
    return 0;
}