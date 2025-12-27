// use of DOM : To modify Content, Style, Structure
// step1 = for access an Element
//         => getElementsById
//         => getElementsByTagName
//         => getElementsByClassName
//         => querSelector // only first matching item (for tag name just use that tag name, for class use ".classname", for id use "#idname")
//         => querSelectorAll()
// step2 = for modifying Content
//         => innerHTML
//         => textContent
//         => innerText

// getElementById
// let hed_ele = document.getElementById("heading")
// hed_ele.innerHTML = "Today I am Learning About Document Object Model"
// hed_ele.textContent = "Today I am Learning About Document"
// hed_ele.innerText = "Today I am Learning About Document Object"
// console.log(hed_ele)

// getElementByTagName
// let hed_ele = document.getElementsByTagName("h1")
// for (let i = 0; i < hed_ele.length; i++){
//     hed_ele[i].textContent = "Today I am Learning About Document"
// }
// console.log(hed_ele)

// getElementsByClassName
let hed_ele = document.getElementsByClassName("head")
for (let i = 0; i < hed_ele.length; i++) {
    hed_ele[i].innerText = "Today I am Learning About Document Object"
}
console.log(hed_ele)