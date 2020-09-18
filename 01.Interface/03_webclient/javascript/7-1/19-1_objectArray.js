//objectArray

function Student(name, korean, math, english, science) { 
    this.name = name;
    this.korean = korean;
    this.math = math;
    this.english = english;
    this.science = science;

    this.getSum = function () {
        return this.korean + this.math + this.english + this.science;
    }
    this.getAverage = function () {
        return this.getSum() / 4;
    }
    this.toString = function () {
        return `${this.name}\t${this.getSum()}\t${this.getAverage()}`;
    }

}

var students = [];

students.push(new Student('윤인성', 90, 83, 76, 89));
students.push(new Student('박찬호', 90, 83, 76, 89));
students.push(new Student('류현진', 90, 83, 76, 89));
students.push(new Student('이세돌', 90, 83, 76, 89));
students.push(new Student('김세진', 90, 83, 76, 89));
students.push(new Student('이하나', 90, 83, 76, 89));

var output = 'name\t총점\t평균\n';
for(var i in students) {
    output += students[i].toString()+ '\n';
}

console.log(output);

/*
name	총점	평균
윤인성	338	84.5
박찬호	338	84.5
류현진	338	84.5
이세돌	338	84.5
김세진	338	84.5
이하나	338	84.5
*/
