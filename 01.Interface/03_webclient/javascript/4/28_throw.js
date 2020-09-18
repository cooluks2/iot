//throw

// 라이브러리 내부
function func() {
    if (true)
        throw "예외가 발생했습니다";
}
    
// 라이브러리 사용
try {
    func();
} catch(exception) {
    console.log(exception);
}
console.log("실행을 완료하였습니다.");

/*
예외가 발생했습니다
실행을 완료하였습니다.
*/

// 배열 뒤에 한번 더 나와서 넘어감