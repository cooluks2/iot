//sum

function sum(n) {
    var s = 0;
    for (var i = 1; i <= n; i++) {
        s += i;
    }
    return s;
}
console.log("1~100 = " + sum(100));
console.log("1~200 = " + sum(200));

/*
1~100 = 5050
1~200 = 20100
*/