//question

var a = 3;
var b = (a % 2 == 0) ? "짝":"홀"

/*
Python
b = "짝" if (a%2==0) else "홀"
*/

console.log("a는 " + b + "수이다.");

a = 2;
b = "2";

console.log("== 비교 : " + (a == b ? "같음":"다름"));  // 암묵적 형변환

/*
a는 홀수이다.
== 비교 : 같음
*/