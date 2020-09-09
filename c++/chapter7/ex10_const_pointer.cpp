#include <iostream>
using namespace std;

int main(int argc, char const *argv[]) {
    // 프로그램에서 사용된 literal데이터 (Hello, c++등)는 전역영역에 저장, 상수이다.
   char test[] = "Hello"; // 문자열 배열(6바이트->마지막 \0 포함, Hello를 복사해와서), 지역변수, stack에 할당, literal데이터를 가져와 복사를 한다.
   char *pstr = "C++"; // 문자열 포인터(8바이트), 지역변수, stack에 할당, 주소값 대입 후 c++이 있는 전역영역을 가리킴
   string str = "World"; // string 객체(32바이트, 실제 데이터와 상관없이 string은 32바이트이다), stack에 할당, string은 불변객체가 아님, insert, remove를 통해 늘릴 수도있고 줄일 수도있다. 내부적으로 동적 데이터를 운영

    // *pstr = 'P'; // 에러남
   cout << test << endl;
   cout << pstr << endl;
   cout << str << endl;

   return 0;
}