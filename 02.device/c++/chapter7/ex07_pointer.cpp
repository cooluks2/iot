#include <iostream>
#include <string>
using namespace std;

class Dog{
public:
    int age;
    string name;

    Dog(){
        age = 1;
        name = "puppy";
    }    
    ~Dog(){ }

    int getAge() { return age;}
    void setAge(int a) { age = a; } 
};

int main(int argc, char const *argv[]) {
   Dog *pDog = new Dog;

   cout << "puppy's age : " << pDog->getAge() << endl;
    // 화살표를 이용하여 객체 멤버 접근

   pDog->setAge(3);
   cout << "puppy's age : " << pDog->getAge() << endl;

   delete pDog;
   return 0;
}