package basic

fun main(args : Array<String>){
    // 읽기전용 - list. 데이터형을 마구 섞어도 된다.
    val lst = listOf(1, "헉", 3.00f, true)
    for (i in 0 .. lst.size- 1){
        println ( lst.get(i).toString() )
    }

    // 수정가능 - List. 데이터형을 미리 정해야 하는 듯.
    println("__________")
    var lstEditable = mutableListOf<String>()

    // add 메소드로 추가
    lstEditable.add("나는야")
    lstEditable.add("우주의")
    lstEditable.add("판타지")
    lstEditable.add("이박사")

    for(s in lstEditable){
        println(s)
    }
    println("__________")

    // remove 메소드로 삭제
    lstEditable.removeAt(0);
    for(s in lstEditable){
        println(s)
    }

    println("__________")

    var m = hashMapOf("고양이" to 1, "강아지" to 2)
    println(m["고양이"])
}