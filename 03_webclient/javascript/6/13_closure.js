//closure

// 지역 변수의 life time

// function test(name) {
//     var output = 'Hello ' + name + '...!';
// }

// console.log(output)

// 오류


// 클로저
function test(name) {
    var output = 'Hello ' + name + '...!';

    return function() {
        console.log(output)
    }
}

test('Javascript')();

/*
Hello Javascript...!
*/


// 클로저 정의

function test(name) {
    var output = 'Hello ' + name + '...!';
    
    return function() {
        console.log(output)
    }
}

var test_1 = test('Node');
var test_2 = test('Javascript');

test_1();
test_2();

/*
Hello Node...!
Hello Javascript...!
*/

// 외부함수가 호출될 때 만들어지고 (호출당 한개 독립적으로)
// 내부함수를 호출했을 때 사용된다.

// 예제(1) 타이머

function outcount() {
    var count = 0;  // 내부함수가 변수를 계속 쓰고 있다. 지워지지 않는다.

    setInterval(function() {
        count++;
        console.log(count + "초 지났습니다.");
    }, 1000); // ms 단위 (1초)
}
outcount();

/*
1초 지났습니다.
2초 지났습니다.
3초 지났습니다.
4초 지났습니다.
...
*/

// 예제(2) 타이머 중지

function outcount(interval) {
    var count = 0;  // 내부함수가 변수를 계속 쓰고 있다. 지워지지 않는다.

    var id = setInterval(function() {
        count++;
        if(count == 2) {
            clearInterval(id);
        }
        console.log(count + "초 지났습니다.");
    }, interval); // ms 단위 (1초)
}
outcount(1000); // 값을 넣어주어서 interval 조정 가능

/*
1초 지났습니다.
2초 지났습니다.
*/
