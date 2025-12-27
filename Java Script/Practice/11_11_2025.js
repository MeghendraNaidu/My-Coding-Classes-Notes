let n = 5;

for (let i = 0; i < n; i++){
    stars = ""
    for (let j = 0; j < 1 + i; j++){
        stars += " *"
    }
    console.log(stars)
}

for (let i = 0; i < n; i++){
    stars = ""
    for (let k = 0; k < 4 - i; k++){
        stars += "  "
    }
    for (let j = 0; j < 1 + i; j++){
        stars += " *"
    }
    console.log(stars)
}