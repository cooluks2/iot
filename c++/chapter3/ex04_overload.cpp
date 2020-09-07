#include <iostream>
using namespace std;
int square(int i)
{
    cout << "square(int) 호출" << endl;
    return i * i;
}
double square(double i)
{
    cout << "square(double) 호출" << endl;
    return i * i;
}
int main(int argc, char const *argv[])
{
    cout << square(10) << endl;
    cout << square(2.0) << endl;
    return 0;
}
