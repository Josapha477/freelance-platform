import { useEffect } from "react"



const Dashboard = () => {


        useEffect(() => {
            document.title = "Dashboard"
        }, [])

    return (
        <div className="flex items-center justify-center
         min-h-screen bg-gray-50 text-black ">
            
            <h1 className="text-5xl font-bold">page Dashboard</h1>
        </div>
    )
}


export default Dashboard