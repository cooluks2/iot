package basic

fun varTest() {
    // 1. 변수의 타입을 미리 정함
    var num : Int // 초기화하지 않아도 됨.
    num = 1

    // 2. 변수의 타입을 정하지 않음
    // 아래는 초기화 반드시 해야함.
    // var number; <-- 에러임
    var number = 2
    // 아래도 에러발생
    // number = "";
    // 즉, 선언과 함께 초기화를 하면 알아서 타입을 정하는 기능정도인 듯.
}

fun valTest() {
    // val은 const와 같은 읽기전용값임.
    val num = 1
    val name : String
    name = ""

    // 에러임. 이미 할당한 값을 재할당 못함.
    // msg = "저장";
}

fun main(args : Array<String>){
    // 변수를 정의하는 방법은 2가지
    // "var, val" 구분해야 함.
    varTest() // R/W 가능변수
    valTest() // ReadOnly 변수
}