#include <iostream>
#include <memory>
#include <string>
using namespace std;

class Dog
{
public:
    int age;
    string name;
    Dog()
    {
        cout << "Dog constructor call" << endl;
        age = 1;
        name = "puppy";
    }
    ~Dog()
    {
        cout << "Dog deconstructor call" << endl;
    }
};

int main(int argc, char const *argv[]) {
    unique_ptr<Dog> buf(new Dog); // startporinter���, �Ҹ��� �ڵ����� ȣ��
//    Dog *pDog = new Dog; // Dog constructor call
//    delete pDog; // Dog deconstructor call
   return 0;
}