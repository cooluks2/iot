//stringcompare

console.log('"korea" > "america" : ' + ("korea" > "america"));
console.log('"Korea" > "america" : ' + ("Korea" > "america"));
console.log('"한글" > "english" : ' + ("한글" > "english"));
console.log('"15" > "12" : ' + ("15" > "12"));
console.log('"015" > "12" : ' + ("015" > "12"));
console.log('"9" > "12" : ' + ("9" > "12"));
console.log('Number("9") > Number("12") : ' + (Number("9") > Number("12")));


/*
"korea" > "america" : true
"Korea" > "america" : false
"한글" > "english" : true
"15" > "12" : true
"015" > "12" : false
"9" > "12" : true
Number("9") > Number("12") : false
*/