import { useEffect, useState } from "react"
import { useParams } from "react-router";
import CustomSpinner from "./CustomSpinner";
import CustomNavbar from "./CustomNavbar";


function Recipes(){
    const [recipes,setrecipes]=useState("")
    const value=useParams()
    useEffect(()=>{
        fetch(`https://dummyjson.com/recipes/${value.id}`)
        .then(res => res.json())
        .then((jsondata)=>{
            console.log(jsondata)
        setrecipes(jsondata)
        })
    })
    return(
        <>
        <CustomNavbar/>
        {recipes?<div style={{display:"flex", margin:"45px 0px 0px 0px"}}><img src={recipes.image} style={{width:"40px", margin:'20px'}}/>
        <div style={{display:"flex", flexDirection:"column", margin:"20px", flexWrap:"wrap"}}>
            <p style={{fontSize:"1.5rem"}}><b style={{fontSize:"1.5rem", fontWeight:"600"}}>Ingredients :</b>{recipes.ingredients}</p>
            <p style={{fontSize:"1.5rem"}}><b style={{fontSize:"1.5rem", fontWeight:"600"}}>Meal Type :</b>{recipes. mealType[0]}</p>
            <p style={{fontSize:"1.5rem"}}><b style={{fontSize:"1.5rem", fontWeight:"600"}}>Name :</b>{recipes.name}</p>
            <p style={{fontSize:"1.5rem"}}><b style={{fontSize:"1.5rem", fontWeight:"600"}}>Rating :</b>{recipes.rating}</p>
            <p style={{fontSize:"1.5rem"}}><b style={{fontSize:"1.5rem", fontWeight:"600"}}>ReviewCount :</b>{recipes.reviewCount}</p>
            <p style={{fontSize:"1.5rem"}}><b style={{fontSize:"1.5rem", fontWeight:"600"}}>PrepTimeMinutes :</b>{recipes.prepTimeMinutes}</p>
            <p style={{fontSize:"1.5rem"}}><b style={{fontSize:"1.5rem", fontWeight:"600"}}>Tags :</b>{recipes.tags}</p>
        </div>
        </div>:<CustomSpinner/>}
        </>
    )


}
export default Recipes