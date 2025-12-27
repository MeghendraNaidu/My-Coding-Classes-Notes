let div_elements = document.getElementsByTagName("div")
div_elements[0].addEventListener("click", function() {
    console.log("Parent")
    div_elements[0].style.backgroundColor = "red"
})
div_elements[1].addEventListener("click", function() {
    console.log("Child")
    div_elements[1].style.backgroundColor = "lightblue"
}, true)
div_elements[2].addEventListener("click", function() {
    console.log("Sub Child")
    div_elements[2].style.backgroundColor = "green"
})