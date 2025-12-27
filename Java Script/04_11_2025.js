for (let i = 0; i < 4; i++){
    stars = ""
    for(let k = 0; k < 4 - i; k++){
        stars += " "
    }
    for (let j = 0; j < 1 + i; j++){
        if(i == 0 || j == 0 || j == i){
            stars += " *"
        }else{
            stars += "  "
        }
    }
    console.log(stars)
}

for (let i = 0; i < 5; i++){
    stars = ""
    for (let k = 0; k< 0 + i; k++){
        stars += " "
    }
    for (let j = 0; j < 5 - i; j++){
        if ( i == 4 || j == 0 || j == 5 - i - 1) {
            stars += " *"
        }
        else{
            stars += "  "
        }
    }
    console.log(stars)
}