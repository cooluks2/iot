#include <iostream>
using namespace std;
int main()
{
    long fact = 1;
    int n;
    cout << "정수를 입력하세요: ";
    cin >> n;
    for (int i = 1; i <= n; i++)
    {
        fact = fact * i;
    }
    cout << n << "! = " << fact << endl;
    return 0;
}
