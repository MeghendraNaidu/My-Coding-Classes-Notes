let a = document.getElementsByTagName("input")
// KeyUp Event
// a[0].addEventListener("keyup", function() {
//     console.log("Event is Listening")
// })

// KeyDown Event
// a[0].addEventListener("keydown", function() {
//     console.log("Event is Listening")
// })

// KeyPress Event
a[0].addEventListener("keypress", function() {
    console.log("Event is Listening")
})

// Blur Event

a[1].addEventListener("blur", function(event){
    console.log(event.target.value)
})
// a[1].addEventListener("focus", function() {
//     console.log(a[1].value)
// })

// Focus Event
a[2].addEventListener("focus", function(event){
    console.log(event.target.value)
})
// a[2].addEventListener("focus", function() {
//     console.log(a[2].value)
// })