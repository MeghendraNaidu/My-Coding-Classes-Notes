// classList is used for adding classes in a element Syntax is "classList.add("classname")"
// For adding attributes we use setAttribute syntax is "setAttribute("class"it is key, "head" and it is value)"

function addstyle(){
    let add = document.getElementsByTagName("h1")
    add[0].classList.add("heading")
    // add[0] = setAttribute("id", "heading")

}
function clearStyle() {
    let remove = document.getElementsByTagName("h1")
    remove[0].classList.remove("heading")
}

function remove() {
    let remove_all = document.getElementsByTagName("h1")
    remove_all[0].classList.toggle("heading")
}