//nameconflict

var score = 100;

function func() {
    var score = 77; // 함수 안에서 변수 선언
    console.log("함수안 score = " + score);  // 지역변수로 본다.
}

func();

console.log("함수밖 score = " + score);
/*
함수안 score = 77
함수밖 score = 100
*/