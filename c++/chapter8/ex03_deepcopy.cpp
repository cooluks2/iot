class MyArray{
public:
    int size;
    int *data;
    MyArray(const MyArray& other){
        size = other.size;
        data = new int[other.size];
        for(int i=0; i<size; i++){
            data[i] = other.data[i]; // 복사 생성자 호출
        }
    }
    ~MyArray(){
        if(data != NULL){
            delete []data;
        }
    }
};