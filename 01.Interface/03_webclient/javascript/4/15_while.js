//while

var size = 1024;
var upload = 0;
while (upload <= size) {
    upload += 200;
    console.log(upload + "M 업로드중.... ");
}
console.log("업로드를 완료하였습니다");

/*
200M 업로드중.... 
400M 업로드중.... 
600M 업로드중.... 
800M 업로드중.... 
1000M 업로드중.... 
1200M 업로드중.... 
업로드를 완료하였습니다
*/