//inherit

class Parent {
    constructor(name) {
        this.name = name;
    }

    print() {
        console.log("이름 : " + this.name);
    }
}


class Child extends Parent {
    constructor(name, age) {
        super(name);  // 오버라이드 시킨것
        this.age = age;
    }

    print() {
        super.print();  // 형식이 Python과 다르다.
        console.log("나이 : " + this.age);
    }

    static sayHello() {
        console.log('Hello~');
    }
}


class GrandChild extends Child {
    constructor(name, age, address) {
        super(name, age);
        this.address = address;
    }
    print() {
        super.print();
        console.log("주소 : " + this.address);
    }
}

var person = new GrandChild("홍길동", 20, "서울");
person.print();
GrandChild.sayHello();  // static 메서드 (인스턴스와 관계없다.)

/*
이름 : 홍길동
나이 : 20
주소 : 서울
Hello~
*/

// 구조를 보기 위해서는 크롬 > F12 > Console 명령창을 이용해서 펼쳐보자.