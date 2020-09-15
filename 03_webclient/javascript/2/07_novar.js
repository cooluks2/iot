//novar

var score = 100; // 이게 없어도 함수 안의 score가 전역변수로 선언된다.

function func() {
    score = 77;  // 전역변수 score에 77을 쓴다.
    console.log("함수안 score = " + score); 
}

func();

console.log("함수밖 score = " + score);
/*
함수안 score = 77
함수밖 score = 77
*/