#include <iostream>
using namespace std;

int main(int argc, char const *argv[])
{
    bool b;
    int x = 3;
    int y = 3;
    cout << std::boolalpha; // 부울린을 true, false로 출력
    
    b = (x == 3) && (y == 3);
    cout << b << endl;
    
    y = 2;
    b = (x == 3) && (y == 3);
    cout << b << endl;

    b = (x == 3) || (y == 3);
    cout << b << endl;

    x = 2;
    b = (x == 3) || (y == 3);
    cout << b << endl;

    b = !(x == 3);
    cout << b << endl;
    
    return 0;
}