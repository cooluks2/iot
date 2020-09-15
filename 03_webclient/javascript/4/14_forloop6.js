//forloop6

// for of 반복문

var arScore = [88, 78, 96, 54, 23];

var sum = 0;

for (let score of arScore) {  // 인덱스는 필요없고 값만 필요할 때
    sum += score;
}

console.log("총점 : " + sum + ", 평균 : " + sum/arScore.length);
console.log(`총점 : ${sum}, 평균 : ${sum/arScore.length}`);

/*
총점 : 339, 평균 : 67.8
총점 : 339, 평균 : 67.8
*/