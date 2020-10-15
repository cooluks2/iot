package basic

fun doubleLoop() {
    for(i in 0 .. 2){
        for (j in 0.. 10){
            if (j == 2) break
            println("i->$i, j->$j")
        }
        println("j loop end")
    }
    println("i loop end")
}

// @레이블 지정 후, break@레이블로 나감
fun ExitDoubleLoop() {
    HereToExit@ for(i in 0 .. 2){
        for (j in 0.. 10){
            if (j == 5) break@HereToExit;
            println("i->$i, j->$j")
        }
        println("j loop end");
    }
    println("i loop end");
}

// 이름없는 함수(람다식)의 리턴
var lambdaReturn = Exit@{
    if(true){
        return@Exit 3
    }
    1000
}

fun main(args : Array<String>){
    doubleLoop();
    println("=================>")
    ExitDoubleLoop();
    println( lambdaReturn() )
}