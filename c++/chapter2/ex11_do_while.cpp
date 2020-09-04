#include <iostream>
using namespace std;

int main(int argc, char const *argv[])
{
    string str;

    do
    {
        cout << "문자열을 입력하세요:";
        // getline(cin, str);

        cin >> str;  // 입력 문자열에 공백이 있는 경우 테스트 -> 예: 안녕 하세요.

        cout << "사용자의 입력: " << str << endl;
    } while (str != "종료");

    return 0;
}