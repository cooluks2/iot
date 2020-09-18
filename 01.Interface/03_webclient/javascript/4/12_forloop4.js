//forloop4

var arScore = [88, 78, 96, 54, 23];

var sum = 0;

for (var st = 0; st < arScore.length; st++) {  // .length : 배열의 길이
    sum += arScore[st];
}

console.log("총점 : " + sum + ", 평균 : " + sum/arScore.length);
console.log(`총점 : ${sum}, 평균 : ${sum/arScore.length}`);

/*
총점 : 339, 평균 : 67.8
총점 : 339, 평균 : 67.8
*/