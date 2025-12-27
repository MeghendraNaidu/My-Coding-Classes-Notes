/*  
Data Types
    1. Primitive ==> string, boolean, undefined, Number, BigInt, Null, Symbol
    2. Non- Primitive ==> Object, Array, Function



*/
// Primitive Data Types

// Number
let age = 20
console.log(typeof(age))

// Number
let salry = 150000.78
console.log(typeof(salry))

// String
let name = "Pavan"
console.log(typeof(name))

// Boolean
let is_getting_high_package = true
console.log(typeof(is_getting_high_package))

// Undefined
let is_salary_fixed = undefined
console.log(typeof(is_salary_fixed))

// Null
let bowl = null
console.log(typeof(null)) // is data type is object

// BigInt
let bigNumber = 123456789012345678901234567890n
console.log(typeof(bigNumber))

// Symbol
let id = Symbol("id")
let anotherID = Symbol("id")
console.log(id === anotherID)

//Non-Primitive Data Types

// Array
var names = ["Basheer", "Sai Kiran", "Abdul"]
console.log(names[1])
console.log(names[2])

var developers = {
    Name : "Basheer",
    Company_Name : "Micro Soft"
}
console.log(developers.Name, developers.Company_Name)
console.log(developers["Name"], developers["Company_Name"])

// Objects
var names1 = [{Name : "Basheer", Company_Name : "Micro Soft"}, {Name : "Sai Kiran", Company_Name : "Google"}, {Name : "Abdul", Company_Name : "FlipKart"}]

console.log(names1[1])
console.log(names1[1].Company_Name)
console.log(names1[1]["Company_Name"])


// Functions

function add() {
    console.log("is this hosted or not")
}
add()

add()
// alert("please enter your data")

function add() {
    console.log("is this hosted or not")
}


// Operators 

let a = 10
console.log(a++) // a = 10 and 10 + 1 // post increment first print "a" value and then it will increment
console.log(++a) // 11 + 1

let b = 5
b += 5
console.log(b)

b -= 5
console.log(b)

let person1 = 5.9
let person2 = 5.5

console.log(person2 > person1)
console.log(person2 == person1) // it is used check only the value
console.log(person1 === person2) //it is used to value and type
