//forloop5

var arScore = [88, 78, 96, 54, 23];

var sum = 0;

for (let ix in arScore) {
    sum += arScore[ix];
}

console.log("총점 : " + sum + ", 평균 : " + sum/arScore.length);
console.log(`총점 : ${sum}, 평균 : ${sum/arScore.length}`);

/*
총점 : 339, 평균 : 67.8
총점 : 339, 평균 : 67.8
*/