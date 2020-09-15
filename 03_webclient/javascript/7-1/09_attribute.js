//attribute

var person = {
    name : '홍길동',
    eat : function(food) {
        console.log(this.name + '이 ' +
                    food + '을/를 먹습니다.');
    }
}

person.eat('피자');

/*
홍길동이 피자을/를 먹습니다.
*/

// 접근자 제한이 없다. 모두다 퍼블릭이다.