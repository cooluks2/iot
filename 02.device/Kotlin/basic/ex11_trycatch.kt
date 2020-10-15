package basic

import java.io.BufferedReader
import java.io.FileReader

fun main(args : Array<String>){
    // try catch를 강제적으로 할 필요가 없다는 말임.
    // 그것보다는 알아서 방어코드를 만들라는 것이 kotlin 철학임.
    try{
        13 / 0
    } catch(e: Exception){
        println(e)
    } finally {
        println("마지막 수행.")
    }

    var zerodivided = 13 / 0;
    println(zerodivided)
}