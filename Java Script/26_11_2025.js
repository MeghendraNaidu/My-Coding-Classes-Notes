// Array Methods
a = []
a.push(1, 2, 3, 4, 5)
console.log(a)
a.pop()
console.log(a)

a.shift()
console.log(a)

a.unshift(1)
console.log(a)


// String Methods

milk_glass = "Milk"
water_glass = "      Water     "

// length of string
console.log(water_glass.length)

// string Concatation
console.log(water_glass + " " + milk_glass)
console.log(water_glass.concat(" ", milk_glass))

// removing spaces in string
console.log(water_glass)

var name1 = "hari"
var name1 = 'hari'
var name1 = `hari` // string interpolation or Template lite
console.log(name1)

// Access through Negative index
console.log(name1.at(-1))

// convert to upper and lower case
console.log(name1.toUpperCase())
console.log(name1.toLowerCase())

// finding askii value
console.log(name1.charAt(1))
console.log(name1.charCodeAt(1))

// Slicing a string - Extracting particular group of character
console.log(name1.slice(1, 4))


// Objects (Create, Access, Update, Delete)
let person = {
    name : "Ram", 
    No_Of_Movies : 67, 
    Awards : 24
}
console.log(person)
// Access using Dot Notation
console.log(person.name)
console.log(person["No_Of_Movies"])

// Update
person.Awards = person.Awards + 1
console.log(person)
person.No_Of_Movies = person.No_Of_Movies + 5
console.log(person)

person["No_Of_Movies"] = person["No_Of_Movies"] + 5
console.log(person)

// Delete
delete person.Awards
console.log(person)

// 2nd Method for creating Objets
let person1 = Object.create(person)
console.log(person1)
person1.name = "Ravi"
console.log(person1)