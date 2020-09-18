//arguments

// sumAll() 함수

function sumAll() {
    var sum = 0;

    // for (var i=0; i<arguments.length; i++) {
    //     sum += arguments[i];
    // }

    for (let value of arguments) {
        sum += value;
    }
    return sum;
}

console.log(sumAll(1,2,3,4,5,6,7,8,9));

/*
45
*/

