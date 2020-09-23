#include <iostream>
using namespace std;

// int array[] = {1, 2, 3, ...};
void initArray(int array[], int size, int value = 0) {
    for(int i=0; i < size; i++) {
        array[i] = value;
    }
}

// 배열1 = 배열2;  // 값 복사 x --> 배열은 call by value가 안됨.

void printArray(int array[],int size) {
    for(int i=0; i < size; i++){
        cout << array[i] << ", ";
    }
    cout << endl;
}


int main(int argc, char const *argv[]) {
    int intList[10];

    initArray(intList, 10, 100); // 100으로 초기화
    printArray(intList, 10);
    
    initArray(intList, 10);  // 0으로 초기화
    printArray(intList, 10);

    return 0;
}