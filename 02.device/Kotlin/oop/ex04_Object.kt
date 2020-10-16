package oop

object SingleTon {
    var printMSG = { msg : String -> println(msg) }
}

class NormalClass{
    var msg: String = "일반객체로 생성하면 이 변수를 액세스 가능함"
    // companion object {} 안에서 구현해야 static 가능
    companion object {
        var staticVar = "staticVar"
        fun staticFunc()= println("이거스태틱 함수임")
    }
}

abstract class fakeClickHandler{
    var msg : String = "abstract 클래스입니다"
    abstract fun onClick()
}

// object 사용예
fun main(args: Array<String>) {
    // 1. 클래스 전체를 싱글톤으로 사용할 때, 마치 java의 static class
    //var 싱글톤변수 = SingleTon()
    SingleTon.printMSG("싱글톤입니다.!")

    val obj = NormalClass()
    println(obj.msg)
    // 아래는 객체이므로 접근하지 못하는 에러코드임
    // 객체.staticVar

    // 2. 자바의 static method를 사용하듯...
    println( NormalClass.staticVar )
    NormalClass.staticFunc()

    // 3.이름없는 클래스 객체를 만들고 사용할 때...
    // 주로 상속받고 필요한 함수만 오버라이드
    var obj2 = object : fakeClickHandler(){
        fun dummyFunc() = "눌렀다"
        override fun onClick() {
            println(dummyFunc())
        }
    }

    obj2.onClick()
}