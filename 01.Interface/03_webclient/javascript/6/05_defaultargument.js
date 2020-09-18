//defaultargument

function sum(n) {
    if (n == undefined)  // defualt 값 줄 때
        n = 100;
    //  n = n || 100;  // 이렇게도 짧게 가능하다. 값이 없다면 결정된 순간의 값인 100이 들어간다.

    var s = 0;
    for (var i = 0; i <= n; i++) {
        s += i;

    }
    return s;
}

console.log("1~10 = " + sum(10));
console.log("1~100 = " + sum());



function sum(n=100) {  // 이제는 defualt 값 이렇게 준다.
    var s = 0;
    for (var i = 0; i <= n; i++) {
        s += i;
    }
    return s;
}
console.log("1~10 = " + sum(10));
console.log("1~100 = " + sum());


/*
1~10 = 55
1~100 = 5050
1~10 = 55
1~100 = 5050
*/
