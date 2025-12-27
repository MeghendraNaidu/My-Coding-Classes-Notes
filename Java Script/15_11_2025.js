// let a = document.createElement("h1")
// a.innerHTML = "Today I am Learning About DOM Concepts"
// document.body.appendChild(a)

// let b = document.createElement("img")
// b.src = "../HTML/images/Billa.jpeg"
// document.body.appendChild(b)

// let c = document.createElement("br")
// document.body.appendChild(c)

// let d = document.createElement("button")
// d.innerHTML = "Change Style"
// document.body.appendChild(d)


let con_ele = document.getElementById("container")
function add() {
    let card = document.createElement("div")
    card.style.backgroundColor = "red"
    card.style.height = "100px"
    card.style.width = "100px"
    card.style.margin = "1px"
    con_ele.appendChild(card )
}

function clearall() {
    con_ele.innerHTML = ""
}
