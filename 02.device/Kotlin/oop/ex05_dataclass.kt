package oop

class DummyClass{
    var DummyData : String? = null
}

data class BasicInfo(var name : String, var age : Int)

data class DetailInfo(var name : String, var age : Int = 30,
                    var dummy :DummyClass? = null )

fun main(args: Array<String>) {
    var data1 = BasicInfo("김모씨", 30)
    var data2 = DetailInfo(name = "박모씨", dummy = DummyClass().apply{ DummyData = "더미입니다" })
    
    var (name1, age1) = data1
    println ("$name1 : $age1")
    
    var (name2, age2, dummy) = data2
    println ("$name2 : ${dummy?.DummyData}")
    
    // 이 부분이 제일 유용함
    var data3 = data2.copy(name = "회장님")
    println ("${data3.toString()}")
}