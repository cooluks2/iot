#include<string>
using namespace std;

class PrintData {
public:
    void print(int i);
    void print(double f);
    void print(string s = "No Data!");  // 디폴트 값 지정은 헤더 파일에서만 지정
};