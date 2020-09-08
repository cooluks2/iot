#include <iostream>
#include <time.h>
using namespace std;

int main() {
    int *ptr;

    srand(time(NULL));
    ptr = new int[10];
    for (int i = 0; i < 10; i++) {
        ptr[i] = rand();
    }

    for (int i = 0; i < 10; i++) {
        cout << ptr[i] << " ";
    }
    cout << endl;
    delete []ptr;
    return 0;
}