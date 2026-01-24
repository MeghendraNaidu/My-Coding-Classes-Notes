import { useEffect, useState } from "react"


function useFetch(url) {
const [data, setdata] = useState("")
    useEffect(() => {
        fetch(url)
            .then(res => res.json())
            .then((jsondata) => {
                console.log(jsondata)
                setdata(jsondata)
            })
    }, [url])
    return(data)
}

export default useFetch