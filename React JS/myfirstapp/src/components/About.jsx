import { useContext } from "react"
import CustomCarousel from "./CustomCarousel"
import CustomNavbar from "./CustomNavbar"
import { Waiter } from "../main"


function About() {
    const data = useContext(Waiter)
    return (
        <>
            <CustomNavbar />
            <CustomCarousel />
            <h1>This is About Page {data}</h1>
        </>
    )
}

export default About