#include <iostream>
#include <string>
using namespace std;
int main(int argc, char const *argv[])
{
    string list[] = {"ȫ�浿", "��浿", "�Ѹ�"};
    for (auto& name : list)
    {
        cout << name << endl;
    }
    return 0;
}
