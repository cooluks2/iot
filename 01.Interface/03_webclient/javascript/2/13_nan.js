//nan

var veryBig = 1234/0;
console.log("veryBig = " + veryBig);  // 1234/0 : Infinity

var noNumber = Math.sqrt(-2);
console.log("noNumber = " + noNumber);  // √(-2) : NaN

/*
veryBig = Infinity
noNumber = NaN
*/