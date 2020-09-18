//prototype

function Student(name, korean, math, english, science) {
    this.name = name;
    this.korean = korean;
    this.math = math;
    this.english = english;
    this.science = science;
} // 생성자 함수 내부에 속성만 넣음


// 한 개의 메서드로 모든 객체가 사용
Student.prototype.getSum = function () {
    return this.korean + this.math + this.english + this.science;
}
Student.prototype.getAverage = function () {
    return this.getSum() / 4;
}
Student.prototype.toString = function () {
    return `${this.name}\t${this.getSum()}\t${this.getAverage()}`;
}


// 강의노트 50p 그림 참고