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
    Person clone{kim}; // 복사 생성자 호출
    cout << "kim의 나이: " << kim.age << " clone의 나이: " << clone.age << endl;
    kim.age = 23;
    cout << "kim의 나이: " << kim.age << " clone의 나이: " << clone.age << endl;
    return 0;
}
