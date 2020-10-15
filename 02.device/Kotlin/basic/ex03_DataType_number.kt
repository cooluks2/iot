package basic

fun main(args : Array<String>){
    // 숫자형 DataType 크기 순으로 선언
    var doubleValue : Double = 10.1111
    var floatValue : Float = 10.1f
    var longValue : Long = 10
    var intValue : Int = 10
    var shortValue : Short = 10
    var byteValue : Byte = 10

    println(doubleValue)
    println(floatValue)
    println(intValue)
    
    // 크기변환 후, 대입 : 캐스팅
    // to대입할크기() 메소드를 사용한다.
    // ** as로 형변환은 기본형에서는 안된다. **
    doubleValue = intValue.toDouble()
    intValue = doubleValue.toInt()
}