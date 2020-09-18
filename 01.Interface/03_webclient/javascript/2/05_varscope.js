//varscope

var global = "전역";  // 맨 뒤로 옮기면 오류가 아닌 undefined
function func() {  // 함수 선언 (호출 뒤에 와도 무방)
    var local = "로컬";
    console.log("함수안 local = " + local);
    console.log("함수안 global = " + global);
}

func(); // 함수 호출
// console.log("함수밖 local = " + local);  // 오류
console.log("함수밖 global = " + global);

// hoisting : JS는 한줄 씩 실행하기 전 식별자 조사를 먼저한다.

/*
함수안 local = 로컬
함수안 global = 전역
함수밖 global = 전역
*/