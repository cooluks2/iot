//objectargument 전과 같은 작업

var human = {
    name: "김상형",
    age: 29
};
function changeName(h) {
    h.name = "김태희";
}
changeName(human);
console.log("name = " + human.name);
console.log("age = " + human.age);

/*
name = 김태희
age = 29
*/