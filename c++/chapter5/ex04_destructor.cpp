#include <string.h>
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
        delete[]s;
    }
};

int main() {
    MyString str("abcdefghijk");
}