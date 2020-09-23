#include <string.h>  // 
#include <string>    // string 클래스 해더 파일
#include <iostream>
using namespace std;

class MyString {
private:
    char *s;  // 포인터
    int size;

public:
    MyString(char *c) {
        size = strlen(c) + 1;
        s = new char[size];  // 동적할당
        strcpy(s, c);
    }

    ~MyString() {
        cout << "~MyString ... delete s" << endl;
        delete[]s;
    }
};

int main() {
    MyString str("abcdefghijk");
}