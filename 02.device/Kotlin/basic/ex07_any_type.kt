package basic

fun main(args : Array <String>){
    // any는 C에서 void*와 같은 역할을 하는 듯.
    // 어떠한 데이터 형의 변수이던간에 담을 수 있는 크기.
    var anything : Any

    anything = 1
    anything = "문자열"
    anything = 111.01010
    anything = 10.00f
    
    // is와 !(not) 연산자로 어떤 데이터 형인지 채크가 가능함.
    if(anything !is String) {
        if (anything is Float) {
            println("float입니다")
        }
    }
}