#include <vector>
#include <iostream>
using namespace std;

int main() {
    vector<int> v1{1, 2, 3, 4, 5};
    vector<int> v2(v1);

    if (v1 == v2) {
        cout << "The two vectors match." << endl;
    }

    return 0;
}