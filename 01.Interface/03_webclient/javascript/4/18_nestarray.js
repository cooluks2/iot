//nestarray

// 다중 루프
var ar = [[0, 1, 2, 3], [4, 5, 6], [7, 8]];

for (var i = 0; i < ar.length; i++) {
    for (var j = 0; j < ar[i].length; j++) {
    console.log("ar[" + i + "][" + j +"] =" + ar[i][j]);
    }
    console.log();
}

/*
ar[0][0] =0
ar[0][1] =1
ar[0][2] =2
ar[0][3] =3

ar[1][0] =4
ar[1][1] =5
ar[1][2] =6

ar[2][0] =7
ar[2][1] =8
*/
