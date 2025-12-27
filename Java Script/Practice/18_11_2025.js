// Right Half Pyramid
for (let i = 0; i < 5; i++) {
    stars = ""
    for (let j = 0; j < 1 + i; j++) {
        stars += " *"
    }
    console.log(stars)
}

// Left Half Pyramid
for (let i = 0; i < 5; i++) {
    stars = ""
    for (let k = 0; k < 4 - i; k++) {
        stars += "  "
    }
    for (let j = 0; j < 1 + i; j++) {
        stars += " *"
    }
    console.log(stars)
}

// Full Pyramid
for (let i = 0; i < 5; i++) {
    stars = ""
    for (let k = 0; k < 4 - i; k++){
        stars += " "
    }
    for (let j = 0; j < 1 + i; j++) {
        stars += " *"
    }
    console.log(stars)
}
// Inverted Right Half Pyramid
for (let i = 0; i < 5; i++) {
    stars = ""
    for (let j = 0; j < 5 - i; j++) {
        stars += " *"
    }
    console.log(stars)
}

// Inverted Left Half Pyramid
for (let i = 0; i < 5; i++) {
    stars = ""
    for (let k = 0; k < 0 + i; k++) {
        stars += "  "
    }
    for (let j = 0; j < 5 - i; j++) {
        stars += " *"
    }
    console.log(stars)
}
// Inverted Full Pyramid
for (let i = 0; i < 5; i++) {
    stars = ""
    for (let k = 0; k < 0 + i; k++) {
        stars += " "
    }
    for (let j = 0; j < 5 - i; j++) {
        stars += " *"
    }
    console.log(stars)
}
// Rhombus Pattern
for (let i = 0; i < 5; i++) {
    stars = ""
    for (let k = 0; k < 0 + i; k++) {
        stars += " "
    }
    for (let j = 0; j < 4; j++) {
        stars += " *"
    }
    console.log(stars)
}
// Diamond Pattern
for (let i = 0; i < 4; i++) {
    stars = ""
    for (let k = 0; k < 4 - i; k++) {
        stars += " "
    }
    for (let j = 0; j < 1 + i; j++) {
        stars += " *"
    }
    console.log(stars)
}
for (let i = 0; i < 5; i++) {
    stars = ""
    for (let k = 0; k < 0 + i; k++) {
        stars += " "
    }
    for (let j = 0; j < 5 - i; j++) {
        stars += " *"
    }
    console.log(stars)
}

// Hourglass Pattern
for (let i = 0; i < 4; i++) {
    stars = ""
    for (let k = 0; k < 0 + i; k++) {
        stars += " "
    }
    for (let j = 0; j < 5 - i; j++) [
        stars += " *"
    ]
    console.log(stars)
}
for (let i = 0; i < 5; i++) {
    stars = ""
    for (let k = 0; k < 4 - i; k++) {
        stars += " "
    }
    for (let j = 0; j < 1 + i; j++) [
        stars += " *"
    ]
    console.log(stars)
}

// Hollow Square Pattern
for (let i = 0; i < 5; i++) {
    stars =""
    for (let j = 0; j < 5; j++) {
        if (i == 0 || j == 0 || i == 4 || j == 4) {
            stars += " *"
        }else{
            stars += "  "
        }
    }
    console.log(stars)
}

// Hollow Full Pyramid
for (let i = 0; i < 5; i++) {
    stars = ""
    for (let k = 0; k < 4 - i; k++) {
        stars += " "
    }
    for (let j = 0; j < 1 + i; j++) {
        if (i == 0 || i == 4 || j == 0 || j == i) {
            stars += " *"
        }else{
            stars += "  "
        }
    }
    console.log(stars)
}

// Hollow Inverted Full Pyramid
for (let i = 0; i < 5; i++) {
    stars = ""
    for (let k = 0; k < 0 + i; k++) {
        stars += " "
    }
    for (let j = 0; j < 5 - i; j++) {
        if (i == 0 || i == 4 || j == 0 || j == 4 - i) {
            stars += " *"
        }else{
            stars += "  "
        }
    }
    console.log(stars)
}

// Hollow Diamond Pyramid
for (let i = 0; i < 4; i++) {
    stars = ""
    for (let k = 0; k < 4 - i; k++) {
        stars += " "
    }
    for (let j = 0; j < 1 + i; j++) {
        if (i == 0 || i == 4 || j == 0 || j == i) {
            stars += " *"
        }else{
            stars += "  "
        }
    }
    console.log(stars)
}
for (let i = 0; i < 5; i++) {
    stars = ""
    for (let k = 0; k < 0 + i; k++) {
        stars += " "
    }
    for (let j = 0; j < 5 - i; j++) {
        if (i == 4 || j == 0 || j == 4 - i) {
            stars += " *"
        }else{
            stars += "  "
        }
    }
    console.log(stars)
}

// Hollow Hourglass Pattern
for (let i = 0; i < 4; i++) {
    stars = ""
    for (let k = 0; k < 0 + i; k++) {
        stars += " "
    }
    for (let j = 0; j < 5 - i; j++) {
        if (i == 0 || i == 4 || j == 0 || j == 4 - i) {
            stars += " *"
        }else{
            stars += "  "
        }
    }
    console.log(stars)
}
for (let i = 0; i < 5; i++) {
    stars = ""
    for (let k = 0; k < 4 - i; k++) {
        stars += " "
    }
    for (let j = 0; j < 1 + i; j++) {
        if (i == 0 || i == 4 || j == 0 || j == i) {
            stars += " *"
        }else{
            stars += "  "
        }
    }
    console.log(stars)
}