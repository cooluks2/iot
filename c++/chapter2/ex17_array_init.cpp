#include <iostream>
using namespace std;

int main()
{
    const int STUDENTS = 5;

    int scores[STUDENTS] = {
        100, 200, 300, 403, 555
    };

    int sum = 0;
    int i;
    double average;

    for (i = 0; i < STUDENTS; i++) {
        sum += scores[i];
    }

    //average = sum / STUDENTS; //������ ��ȯ
    average = sum / (double)STUDENTS;
    cout << "���� ���= " << average << endl;
    
    return 0;
}
