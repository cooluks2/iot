#include <iostream>
#include <string>
using namespace std;
class Person
{
public:
    int age;
    Person(int a) : age(a) {}
};

int main(int argc, char const *argv[])
{
    Person kim{21};
    Person clone{kim}; // ���� ������ ȣ��
    cout << "kim�� ����: " << kim.age << " clone�� ����: " << clone.age << endl;
    kim.age = 23;
    cout << "kim�� ����: " << kim.age << " clone�� ����: " << clone.age << endl;
    return 0;
}
