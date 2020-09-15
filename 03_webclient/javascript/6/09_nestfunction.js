//nestfunction

// 함수 고급

function sum(n) {
    function add(a, b) {
    return a + b;
    }
    var s = 0;
    for (var i = 0; i <= n; i++) {
    s = add(s, i);
    }
    return s;
}
console.log("1~100 = " + sum(100));
console.log("2 + 3 = " + add(2 + 3));// 에러

/*
1~100 = 5050
c:\workspace\03_webclient\javascript\6\09_nestfunction.js:14
console.log("2 + 3 = " + add(2 + 3));// 에러
        ^

ReferenceError: add is not defined
...
*/

/*
// closer
function outer() {
var outvalue = 5678;
function inner() {
var invalue = 1234;
console.log("outvalue = " + outvalue);
}
inner();
console.log("invalue = " + invalue);// 에러
}
outer();
*/