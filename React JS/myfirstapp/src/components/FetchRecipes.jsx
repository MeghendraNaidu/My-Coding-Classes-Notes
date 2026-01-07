import { useEffect, useState } from "react"
import CustomSpinner from "./CustomSpinner"
import { Link } from "react-router"


function FetchRecipes() {
    const [recipes, setrecipes] = useState("")
    useEffect(()=> {
        fetch('https://dummyjson.com/recipes')
        .then(res => res.json())
        .then((jsondata)=> {
            console.log(jsondata)
            setrecipes(jsondata.recipes)
        })
    }, [])
    return(
        <>
        {recipes.length>0?<div style={{display:"flex", flexWrap:"wrap"}}>
        {recipes.map(each => <div style={{width:"19.2%", margin:"5px", display:"flex", flexDirection:"column"}}>
        <Link to={`/recipes/${each.id}`}><img src={each.image} style={{width:"100%", margin:"5px"}}/></Link>
        <h6 style={{textAlign:"center"}}>{each.name}</h6>
        </div>)}
        </div>:<CustomSpinner/>}
        </>
    )
}

export default FetchRecipes