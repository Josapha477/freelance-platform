import { useEffect } from "react"


const Mission = () => {

    useEffect(() => {
       document.title = "mission" 
    },[])

    return (
        <div className="min-h-screen flex justify-center 
        items-center text-black font-bold bg-gray-50">
            <h1 className="text-4xl">Page de Mission</h1>
        </div>
    )
}


export default Mission