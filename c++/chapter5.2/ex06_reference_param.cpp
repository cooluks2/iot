#include <iostream>
using namespace std;

class Pizza {
public:
    int size;
    Pizza(int s) : size(s) {}
};

void makeDouble(Pizza& p) {
    p.size *= 2;
}

int main() {
    Pizza pizza(10);
    makeDouble(pizza);
    cout << pizza.size << "��ġ ����" << endl;
    
    return 0;
}
