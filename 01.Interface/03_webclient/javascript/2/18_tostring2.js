//tostring2

var staff = "김상형 : ";
var salary = 320;
var bonus = 160;
console.log(staff + salary + bonus + "만원");  // 왼쪽부터 암시적 변환

var staff = "김상형 : ";
var salary = 320;
var bonus = 160;
console.log(staff + String(salary + bonus) + "만원");

var staff = "김상형 : ";
var salary = 320;
var bonus = 160;
console.log(salary + bonus + "만원" + staff);  // 왼쪽부터 암시적 변환

/*
김상형 : 320160만원
김상형 : 480만원
480만원김상형 : 
*/