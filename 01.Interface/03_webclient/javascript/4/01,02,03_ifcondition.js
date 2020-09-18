//ifcondition

var num = 14;
if (num % 2 == 0)
    console.log(num + "는 짝수입니다.");
// 한 줄만 {} 생략가능

var num = 4;
if (num % 2 == 0) {
    console.log(num + "는 짝수입니다.");
    console.log("짝수는 2로 나누어 떨어지는 수입니다.");
}

var num = 4;
if (num % 2 == 0)
    console.log(num + "는 짝수입니다.");
    console.log("짝수는 2로 나누어 떨어지는 수입니다.");


/*
14는 짝수입니다.
4는 짝수입니다.
짝수는 2로 나누어 떨어지는 수입니다.
4는 짝수입니다.
짝수는 2로 나누어 떨어지는 수입니다.
*/