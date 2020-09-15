//ifelseif

var num = 2;

if (num == undefined) {
    console.log("숫자를 입력해 주십시오.");
} else {
    if (num > 0) {
        console.log(num + "는 양수입니다.");
    } else if (num < 0) {
        console.log(num + "는 음수입니다.");
    } else {
        console.log(num + "은 틀림없이 0입니다.");
    }
}

// Python은 elif

/*
2는 양수입니다.
*/