//studentObject

function Student(name, korean, math, english, science) {  // student 객체의 student 생성자 함수
    this.name = name;
    this.korean = korean;
    this.math = math;
    this.english = english;
    this.science = science;


    // 메서드 생성
    this.getSum = function () {
        return this.korean + this.math + this.english + this.science;
    }
    this.getAverage = function () {
        return this.getSum() / 4;
    }
    this.toString = function () {
        return `${this.name}\t${this.getSum()}\t${this.getAverage()}`;
    }


}  // 자동으로 this의 값이 리턴

var student = new Student('김세진', 90, 83, 76, 89);
console.log(student)
// Heap에 새로운 인스턴스가 생성되고 this에 배정
// new 생성자() 가 있어야 새로운 인스턴스가 생성된다.

var student2 = Student('김세진', 90, 83, 76, 89);
console.log(student2)
// new가 없으면 일반 함수 호출과 같다. (리턴값이 없으니 undefined)

/*
Student {
  name: '김세진',
  korean: 90,
  math: 83,
  english: 76,
  science: 89,
  getSum: [Function],
  getAverage: [Function],
  toString: [Function]
}
undefined
*/