import { useEffect } from "react"


const CreateProfile = () => {

    useEffect(() => {
      document.title = "add-profile"  
    }, [])

    return (
        <div className="bg-gray-50 flex items-center 
        justify-center min-h-screen">
            <div className="flex w-7/8 shadow-2xl h-7/8">
                <form className='gap-10 flex flex-col
                 w-full justify-center items-center'>
                    <div>
                        <label htmlFor="first_name"
                            className="label">first_name</label>
                        <input id="first_name" type="text" placeholder="first_name"
                            className="input bg-blue-500 hover:bg-blue-700" />
                    </div>
                    <div>
                        <label htmlFor="last_name"
                            className="label">last_name</label>
                        <input type="text" 
                            className="input hover:bg-blue-700" />
                    </div>
                    <div>
                        <label htmlFor="email">Email</label>
                        <input type="text" className="input hover:bg-blue-700"/>
                    </div>
                    <div>
                        <label htmlFor="password">Password</label>
                        <input type="text" className="input hover:bg-blue-700"/>
                    </div>
                </form>
            </div>
        </div>
    )
}

export default CreateProfile