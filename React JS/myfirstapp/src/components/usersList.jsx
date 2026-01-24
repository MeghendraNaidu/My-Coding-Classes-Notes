import "./usertList.css"

let users = ["Nani", "Venkat", "Yaswanth", "Murali", "Ram"]

function UserList() {
    return (
        <>
            {
                users.map((val, index) => <h3 key={index}><Greeting user={val} /></h3>)
            }

        </>
    )
}
export default UserList

function Greeting(props) {
    return (<div className="theme">
        Happy New Year {props.user}
    </div>)
}
