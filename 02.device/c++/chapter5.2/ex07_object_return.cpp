#include <iostream>
using namespace std;
class Pizza {
public:
    int size;
    Pizza(int s) : size(s) {}
};

Pizza makePizza() {
    Pizza p(10);
    return p;
}

int main() {
    Pizza pizza = makePizza();

    cout << pizza.size << "인치 피자" << endl;

    return 0;
}
