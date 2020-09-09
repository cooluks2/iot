#include <iostream>
#include <string>
using namespace std;

class Rectangle{
private:
    int length;
    int width;
public:
    // Rectangle(int length=30, int width=40){
    //     this->length = length;
    //     this->width = width;
    // }    

    // 멤버 초기화 리스트로 초기화하기
    Rectangle(int length=30, int width=40) : length(length), width(width){
    } // this를 쓰지 않아도 규칙이 있어 변수를 받아옴
      //length(length) : 괄호 밖 -> 멤버변수, 괄호 안 -> 규칙상 지역변수
    ~Rectangle() {}
    void setLength(int length){
        this->length = length;
    }
    int getLength(){
        return this->length;
    }
    void setWidth(int width){
        this->width = width;
    }
    int getWidth(){
        return this->width;
    }
};

int main(int argc, char const *argv[]) {
   Rectangle rect;

   cout << "rectangle's width : " << rect.getWidth() << endl;
   cout << "rectangle's length : " << rect.getLength() << endl;

   rect.setLength(50);
   rect.setWidth(60);

   cout << "rectangle's width : " << rect.getWidth() << endl;
   cout << "rectangle's length : " << rect.getLength() << endl;
   return 0;
}