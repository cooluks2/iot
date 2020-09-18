//student2

class Student {
    constructor(name, age) {  // 생성자를 constructor() 함수로 정의
        this.name = name;
        this.age = age;
    }

    printProfile(){  // 자동으로 프로토타입 메서드로 넘어간다. (function X!!!)
        console.log(`이름 : ${this.name}, 나이 : ${this.age}`);
    }
}

var s1 = new Student("홍길동", 20);
s1.printProfile();

console.log("printProfile" in s1.__proto__)
console.log("printProfile" in Student.prototype)
// 둘다 prototype이 있다.


/*
이름 : 홍길동, 나이 : 20
true
true
*/