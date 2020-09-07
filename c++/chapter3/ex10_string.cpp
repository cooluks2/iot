#include <iostream>
#include <string>
using namespace std;
int main(int argc, char const *argv[])
{
    string list[] = {"홍길동", "고길동", "둘리"};
    for (auto& name : list)
    {
        cout << name << endl;
    }
    return 0;
}
