#include<iostream>
#include<string>
#include "PrintData.hpp"
using namespace std;

void PrintData::print(int i) {
    cout << i << endl;
}

void PrintData::print(double f) {
    cout << f << endl;
}

void PrintData::print(string s) {
    cout << s << endl;
}