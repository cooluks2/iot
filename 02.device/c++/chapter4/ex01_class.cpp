#include <iostream>
#include <string>
using namespace std;

class Circle
{
public:
    int radius;   // ������
    string color; // ����
    double calcArea() {  // Python�� �޸� self �Ű� ���� ����.
        return 3.14 * radius * radius;  // ��� ���� ���ٽ� �ٷ� ���
    }
};

int main(int argc, char const *argv[])
{
    Circle obj; // ��ü ����
    obj.radius = 100;
    obj.color = "blue";
    // obj.area = 40;  // ���� -- �������� ��� �߰� �Ұ�
    cout << "���� ���� " << obj.calcArea() << endl;
    return 0;
}
