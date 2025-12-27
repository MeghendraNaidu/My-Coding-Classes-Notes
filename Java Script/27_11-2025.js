let person = {
    name : "Nani",
    age : 25, 
    Awards : 12, 
    No_of_backlogs : 3
}
console.log(person.name)
console.log(person["name"])

console.log(person.age = 22)
console.log(person["age"] = 30)

// delete person.name
// console.log(person)
// delete person["age"]
// console.log(person)

for (let keys in person) {
    console.log(keys, person[keys])
}

console.log(Math.floor(1.0))
