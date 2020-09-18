//objectref

var human = {
    name: "김상형",
    age: 29
};

var kim = human;
kim.name = "김태희";

console.log("name = " + human.name);
console.log("age = " + human.age);

/*
name = 김태희
age = 29
*/