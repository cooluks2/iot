//extraargument

function add(a, b) {
    return a + b;
}

console.log(add(2, 3));
console.log(add(2, 3, 4));  // 4는 무시됨
console.log(add(2));  // 나머지 하나는 undefined

/*
5
5
NaN
*/