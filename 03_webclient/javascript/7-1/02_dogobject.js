//dogobject

var dog = {
    type: "치와와",
    weight: 2,
    male: true
};

console.log("종류 = " + dog.type);
console.log("무게 = " + dog.weight);
console.log("숫컷 = " + dog["male"]);
// 변수에 문자열이 있을 때 이렇게도 사용 가능

/*
종류 = 치와와
무게 = 2
숫컷 = true
*/