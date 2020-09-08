#include <vector>
#include <iostream>
using namespace std;
int main() {
    vector<int> fibo = {0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89};
    for (auto& number: fibo) {
        cout << number << ' ';
    }
    cout << endl;
    return 0;
}