#include <iostream>
#include <string>
using namespace std;
int main(int argc, char const *argv[])
{
    string s1, addr;
    cout << "이름을 입력하세요: ";
    cin >> s1;
    cin.ignore(); // 엔터키 제거

    cout << "주소를 입력하세요: ";
    getline(cin, addr);
    
    cout << addr << "의" << s1 << "씨 안녕하세요?" << endl;
    return 0;
}