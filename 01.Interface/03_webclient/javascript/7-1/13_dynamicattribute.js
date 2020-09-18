//dynamicattribute

var student = { };

// 동적으로 속성 추가

student.name = '홍길동';
student.hobby = '악기';
student.special = '프로그래밍';
student.department = '생명공학과';
console.log(student);

for(let key in student) {
    console.log(key, student[key]);
}


/*
{ name: '홍길동', hobby: '악기', special: '프로그래밍', department: '생명공학과' }
name 홍길동
hobby 악기
special 프로그래밍
department 생명공학과
*/


// ...이어서 (속성 추가)

student.toString = function() {
    for(var key in this) {
        if(key != 'toString') {
            console.log(key + '\t' + this[key])
        }
    }
}

student.toString();

/*
name	홍길동
hobby	악기
special	프로그래밍
department	생명공학과
*/


// ...이어서 (속성 제거)


delete student.hobby
student.toString();

/*
name	홍길동
special	프로그래밍
department	생명공학과
*/