//tonumber

var korean = "82";
var english = "75";
var total = Number(korean) + Number(english);
console.log("총점은 " + total + "이다.");

var korean = "82점";
var english = "75점";
var total = parseInt(korean) + parseInt(english); // 정수부분만 읽는다.
console.log("총점은 " + total + "이다.");

/*
총점은 157이다.
총점은 157이다.
*/