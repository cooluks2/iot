//nestobject

var human = {
    name: "김상형",
    age: 29,
    address: {
        city: "하남시",
        dong: "덕풍동",
        bunji: 638
    }
};
console.log("name = " + human.name +
    ", 나이 = " + human.age);
console.log("주소 = " + human.address.city + " " +
    human.address.dong + " " +
    human.address.bunji);

/*
name = 김상형, 나이 = 29
주소 = 하남시 덕풍동 638
*/