//intro

var human = {
    name: "김상형",
    age: 29,
    intro: function() {
        console.log("name = " + this.name);
        console.log("age = " + this.age);
    }
}

human.intro();
console.log(human);  // 객체의 인스턴스를 출력

/*
name = 김상형
age = 29
{ name: '김상형', age: 29, intro: [Function: intro] }
*/