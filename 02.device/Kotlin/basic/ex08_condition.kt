package basic

fun ifExample() {
    // 비교문
    //var a : Any? = "aaaa";
    //var a : Any? = 10.00f;
    //var a : Any? = 8;
    var a : Any? = null;

    if (a == "aaaa"){ // ==를 이용한 값비교
        println ("문자:" + a )

    } else if( a is Float ) { // is를 이용한 형비교
        println ("숫자:" + a)

    } else if (a in (0..9) ){ // in을 이용한 범위비교
        println ("0-10까지 숫자")

    } else if (a == null ){
        println ("null!")
    }
}

fun loopExample() {
    // 반복문 for: in과 (시작..끝)으로 반복가능
    for (i in (0..10)){
        println ("i -> " + i )
    }

    // 반복문 while: while(조건){}
    var i : Int = 0;
    while(i < 10){
        i++; println ("$i 입니다.")
    }
}

fun caseExample() {
    //var obj : Any? = "aaaa";
    var obj : Any? = 10.00f
    //var obj : Any? = 8;

    when(obj){
        "aaaa"      ->{println ("문자:" + obj )}
        is Float    ->{println ("숫자:" + obj)}
        in (0 .. 9) ->{println ("0-10까지 숫자")}
        else        ->{println ("???")}
    }
}

fun main(args : Array<String>){
    ifExample()
    loopExample()
    caseExample()
}