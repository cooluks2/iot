//accessmember

var human = {
    name: "김상형",
    age: 29
};

var name = 'age';

console.log("name = " + human["name"]);
console.log("age = " + human["age"]);
console.log("name = " + human[name]);

/*
name = 김상형
age = 29
name = 29
*/