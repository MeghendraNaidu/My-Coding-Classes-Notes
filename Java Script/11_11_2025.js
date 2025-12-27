// Function Definition
// Function is a block of code which is  used to perform a specific task when someone calls/invoke it

// You can define a function using the function keyword followed by function name, parameters(optional), 
// and the function body enclosed by {}


// function greet() {
//     console.log("This is a Function Definition")
// }
// greet()

// Arrow Function
// let a = () => {
//     console.log("This is a Arrow Function")
// }
// a() // Invoke

// IIFE
// IIFE is a block of code which is used to perform specific task it can be invoked when its define

// (function(){
//     console.log("This is IIFE")
// }) ()

// Genarator Function
// function* greet(){
//     yield 1 + 2
//     yield 2 - 5
//     yield 2 * 4
//     yield 2 / 4
// }
// let store = greet() // object function
// console.log(store.next())  // first operation
// console.log(store.next())  // second operation
// console.log(store.next())  // third operation
// console.log(store.next())  // fourth operation

// console.log(greet().next())  // It perform only the first operation
// console.log(greet().next())  // It perform only the first operation
// console.log(greet().next())  // It perform only the first operation

// Constructor Function
// function greet() {
//     console.log("This is Function Declaration")
// }
// greet()

// function greet() {
//     return "This is Function Declaration"
// }
// let store = greet()
// console.log(store)

// function greet() {
//     this.name = "This is Constructor Function" // this means no need to return it will return automatically
//     this.age = 22
// }
// let store = new greet() // constructor function can be invoked by the
// console.log(store)
// console.log(store.name)
// console.log(store.age)

// Higher Order Function
// function add(a, b) {
//     return a + b
// }

// function sub(a, b) {
//     return a - b
// }

// function mul(a, b) {
//     return a * b
// }

// function operation(action, a, b) {
//     let result = action(a, b)
//     console.log(result)
// }
// operation(add, 3, 4)  // HOF which takes anotherfunction as an argument
// operation(sub, 4, 5)
// operation(mul, 2, 8)

// Anonymus Function is a function which is used to define without name
// let a = function() {
//     console.log("This is Anonymus Function")
// }
// a() // Call or Invoke

// DOM means Document Object Model which is used to manipi=ulate style, html structure, content

