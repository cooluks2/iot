//funcargument

var add = function(a, b) {
    return a+b;
}

var multi = function(a, b) {
    return a*b;
}

function calc(a, b, f) {
    return f(a,b);
}

console.log("2 + 3 = " + calc(2, 3, add));
console.log("2 * 3 = " + calc(2, 3, multi));

console.log("2 + 3 = " + calc(2, 3, (a,b)=>a+b));  // Python의 람다함수와 비슷
console.log("2 * 3 = " + calc(2, 3, (a,b)=>a*b));  // JS의 화살표 함수 (인수)=>(리턴값)

/*
2 + 3 = 5
2 * 3 = 6
2 + 3 = 5
2 * 3 = 6
*/

// 함수를 리턴하는 함수

function outer() {
    return function() {
        console.log('Hello Function...!');
    };
}

// 호출 1
outer()();
// 호출 2
var fn = outer();
fn();

/*
Hello Function...!
Hello Function...!
*/