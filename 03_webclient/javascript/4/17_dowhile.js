//dowhile

// 최소 한 번은 실행

var sum = 0;
var num;
do {
    num = prompt("숫자를 입력하세요(끝낼 때는 0)", "2");
    sum += Number(num);
} while (num != 0);

console.log("입력한 모든 숫자의 합 = " + sum);

// ???
