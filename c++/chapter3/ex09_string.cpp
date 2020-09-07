#include <iostream>
#include <string>

using namespace std;

int main(int argc, char const *argv[])
{
    string s = "When in Rome, do as the Romans.";
    // 읽기
    for (auto& ch : s)  // char &ch = s[i]
    {
        cout << ch << ' ';
    }
    cout << endl;

    for (auto ch : s)  // char ch = s[i]
    {
        cout << ch << ' ';
    }
    cout << endl;

    // 쓰기
    for (auto& ch : s)  // char &ch = s[i]
    {
        ch = 'T';
    }
    cout << s << endl;

    for (auto ch : s)  // char ch = s[i]
    {
        ch = 'W';
    }
    cout << s << endl;

    return 0;
}
