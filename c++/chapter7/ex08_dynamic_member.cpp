#include <iostream>
#include <string>
using namespace std;

class Dog{
private:
    int *pAge; // 멤버변수
    int *pWeight;
public:
    Dog(){
        pAge = new int{1};
        pWeight = new int{10};
    }
    ~Dog(){
       // 만약 pAge와 pWeight delete를 하지 않게되면 Dog가 가리키는 객체만
       // 사라지게 되어 pAge와 pWeight 의 저장공간은 남게되어 garbage가 생김
        delete pAge;
        delete pWeight; 
    }
    int getAge(){ return *pAge; }
    void setAge(int a) { *pAge = a; }
    int getWeight(){ return *pWeight; }
    void setWeight(int w) { *pWeight = w; }
};

int main(int argc, char const *argv[]) {
   Dog *pDog = new Dog;
   cout << sizeof(pDog) << endl; // pDog포인터 변수의 크기, 8출력
   cout << sizeof(*pDog) << endl; // pDog포인트하는 인스턴스의 크기, 16출력

   cout << "puppy's age : " << pDog->getAge() << endl;

   pDog->setAge(3);
   cout << "puppy's age : " << pDog->getAge() << endl;

   delete pDog;   
   return 0;
}