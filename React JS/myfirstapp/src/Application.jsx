import React from "react"

import CustomSpinner from './components/CustomSpinner.jsx'
import CustomCarousel from "./components/CustomCarousel.jsx"
import CustomNavbar from "./components/CustomNavbar.jsx"

class Application extends React.Component {
    constructor() {
        super()
        this.state = {
            products : []
        }
    }
    componentDidMount() {
        console.log("Side Effects")
        fetch('https://dummyjson.com/recipes')
        .then(res => res.json())
        .then((response)=> {
            this.setState({products : response.recipes})
        })
    }

    render() {
        return(
            <>
            <CustomNavbar/>
            <CustomCarousel/>
            {this.state.products.length>0?<div style={{display:"flex", flexWrap:"wrap"}}> 
            {this.state.products.map(each=><div style={{display:"flex", flexDirection:"column", margin:"5px", width:"19%"}}>
            <img src={each.image} style={{width:"100%"}}/>
            <h6>{each.name}</h6>
            </div>)}
            </div>:<CustomSpinner/>}
            </>
        )
    }
}

export default Application 