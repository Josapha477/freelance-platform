import { Link } from "react-router-dom"
import { MessageSquare } from "lucide-react"

export default function Navbar() {

    return (
        <div className="navbar bg-base-100 shadow-sm top-0 fixed z-10">
  <div className="navbar-start">
    <div className="dropdown">
      <div tabIndex={0} role="button" className="btn btn-ghost btn-circle">
        <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"> <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M4 6h16M4 12h16M4 18h7" /> </svg>
      </div>
      <ul tabIndex="-1"
        className="menu menu-sm dropdown-content bg-base-100 rounded-box z-1 mt-3 w-52 p-2 shadow">
        <li><a>Homepage</a></li>
        <li><a>Portfolio</a></li>
        <li><a>About</a></li>
      </ul>
    </div>
  </div>
  <div className="navbar-center">
    <a className="btn btn-ghost text-xl">daisyUI</a>
  </div>
  <div className="navbar-end">
    <button className="btn btn-ghost btn-circle">
      <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"> <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" /> </svg>
    </button>
    <button className="btn btn-ghost btn-circle">
      <div className="indicator">
        <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"> <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9" /> </svg>
        <span className="badge badge-xs badge-primary indicator-item"></span>
      </div>
    </button>
  </div>
</div>
    )


    // return (
    //     <header className="fixed top-0 
    //         w-full bg-opacity-100 shadow
    //         z-50 backdrop-blue-2xl
    //       bg-white/10 backdrop-blur-md border-b
    //       border-white/20">
    //         <div className="max-w-7xl mx-auto px-6 py-4 flex 
    //                          items-center justify-between">
    //         <div className="text-2xl font-bold text-blue-600">
    //             ASTER
    //         </div>
    //         <nav className="md:flex space-x-4 font-bold text-extrabold justify-between text-black">
    //                 <Link to={'/'}>Accueil</Link>
    //                 <Link to={`/profile/${2}`}>Profile</Link>
    //                 <Link to={"/dashboard"}>dashboard</Link>
    //                 <Link to={"/createprofile"}>Add Profile</Link>
    //                 <Link to={"/message"}><MessageSquare/></Link>
    //                 <Link to={"/mission"} className="">Mission</Link>
    //             </nav>
    //             {/* <button className=" 
    //                  px-5 py-2 rounded-lg text-black
    //                  "><SunIcon></SunIcon></button> */}
    //             </div>
    //     </header>
    // )
}