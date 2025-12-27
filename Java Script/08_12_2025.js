// Call Apply Bind

function greet(...a) {
    console.log(this.name, this.age, a)
}

let person1 = {
    name : "Nani",
    age : 22
}

let person2 = {
    name : "Meghendra",
    age : 23
}

let person3 = {
    name : "Venkat",
    age : 21
}

greet.call(person1, 1, 2, 3, 4, 5)
greet.apply(person2, [1, 2, 3, 4, 5])
let res = greet.bind(person3, 1, 2, 3, 4, 5)
res()