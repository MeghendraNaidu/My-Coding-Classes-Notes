// console.log(a())
// console.log(b())

// function a(){
//     return "Function Declaration"  // For this we will get output like this "Function Decalration"
// }

// var b = function() {
//     return "Function Expression"  // For this we will get an error like "b is not a function"
// }

// let greet = function() {
//     return "Hello!"
// }

// console.log(typeof greet)  // for this we will get an output like this "function"
// console.log(greet.name)  // for this we will get an output like this "greet"

// let result = (function(x,y) {
//     return x * y
// })(3, 4)

// console.log(result)  // for this we will get an output like this "12"

// let user = {
//     name: "Noor",
//     say: () =>{
//         console.log(this.name)
//     }
// }
// user.say()  // for this we will get an output like this "undefined"

// function * counter() {
//     yield 1;
//     yield 2;
//     return 3;
// }
// let gen = counter()
// console.log(gen.next())  // for this we will get an output like this "{ value: 1, done: false }"
// console.log(gen.next())  // for this we will get an output like this "{ value: 2, done: false }"
// console.log(gen.next())  // for this we will get an output like this "{ value: 3, done: true }"

// function greet(name) {
//     return "Hello" + name
// }

// function execute(fn, value) {
//     return fn(value)
// }

// console.log(execute(greet, "Student"))  // for this we will get an output like this "HelloStudent"

// let count = 0
// function add(a, b){
//     return a + b
// }

// console.log(add(3, 4))  // for this we will get an output like this "7"
// console.log(count)  // for this we will get an output like this "0"

// function multiply(a, b = 5){
//     return a * b
// }

// console.log(multiply(3))  // for this we will get an output like this "15"
// console.log(multiply(3, 2))  // for this we will get an output like this "6"

// function factorial(n) {
//     if (n === 1) return 1
//     return n * factorial(n - 1)
// }

// console.log(factorial(4))  // for this we will get an output like this "24"

// function printResult(fn, num) {
//     console.log(fn(num))
// }

// function double(n) {
//     return n * 2
// }

// printResult(double, 10)  // for this we will get an output like this "20"


for (let i = 0; i<= 4; i++){
    let result = "";
    for (let j = 0; j<=i; j++){
        result += " *";
    }
    console.log(result)
}