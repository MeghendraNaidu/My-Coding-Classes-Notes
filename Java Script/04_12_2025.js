arr = [10, 20, 30, 40, 50]
// let result = arr.map(function(each) {
//     return each * 2
// })
// console.log(result)

// let result = arr.map((each) => (each * 2))
// console.log(result)

// let result = arr.filter(function(each_ele) {
//     if(each_ele >= 40) {
//         return each_ele
//     }
// })
// console.log(result)
// console.log(arr)

// let res = arr.reduce((prev, prest) => {
//     console.log(prev, prest)
//     return prev + prest
// }, 10)
// console.log(res)

arr = [20, 30, 40, 51, 12, 11, 6]
console.log(arr.sort((a, b) => {
    return a - b
}))