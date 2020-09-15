//blockscope

for (var i = 0; i < 3; i++) {
    var k = 1234;
    console.log("i = " + i);
}

console.log("i = " + i + " , k = " + k);  // 여전히 살아있다.

// let 키워드 : 블록 범위 변수 선언 (ES6부터 추가)
// 블록 시작 ~ 블록 벗어날 때

/*
i = 0
i = 1
i = 2
i = 3 , k = 1234
*/