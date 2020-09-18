//in

var product = {
    name: 'Microsoft Office 2016',
    price: '15,000,000원',
    language: '한국어',
    supportOS: 'Win 32/64',
    subscription: true
}

for (var key in product) {
    console.log(key + ' : ' + product[key]);
}

/*
name : Microsoft Office 2016
price : 15,000,000원
language : 한국어
supportOS : Win 32/64
subscription : true
*/

