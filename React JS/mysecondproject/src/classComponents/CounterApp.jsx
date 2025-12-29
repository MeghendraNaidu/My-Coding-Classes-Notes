import React from "react"

class CounterApp extends React.Component{
    state = {
        count : 0
    }

    increment = ()=> {
        console.log("Increment method is Triggered")
        this.setState({count:this.state.count + 1})
    }

    decrement = ()=> {
        console.log("Decrement method is Triggered")
        this.setState({count:this.state.count - 1})
    }

    render() {
        return(
            <div style={{margin:"10%"}}>
                <h1>counter app</h1>
                <div style={{display:"flex", gap:"10px"}}>
                    <button onClick={this.decrement}>Decreament</button>
                    <p>Count : {this.state.count}</p>
                    <button onClick={this.increment}>Increament</button>
                </div>
            </div>
        )
    }
}

export default CounterApp