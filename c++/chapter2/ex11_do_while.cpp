#include <iostream>
using namespace std;

int main(int argc, char const *argv[])
{
    string str;

    do
    {
        cout << "���ڿ��� �Է��ϼ���:";
        // getline(cin, str);

        cin >> str;  // �Է� ���ڿ��� ������ �ִ� ��� �׽�Ʈ -> ��: �ȳ� �ϼ���.

        cout << "������� �Է�: " << str << endl;
    } while (str != "����");

    return 0;
}