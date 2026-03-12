import Login from "./auth/Login";
import Register from "./auth/Register";
import { Routes, Route } from "react-router-dom";
import Home from "./pages/Home";
import  Profile  from "./pages/Profile";
import Dashboard from "./pages/Dashboard";
import CreateProfile from "./pages/CreateProfile";
import Message from "./pages/Message";
import Mission from "./pages/Mission";
import Navbar from "./components/Navbar";


function App() {
  return (
    <div className="min-h-screen">
      <Navbar></Navbar>
    <div className="pt-20">
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/profile/:id" element={<Profile/>} />
          <Route path="/dashboard" element={ <Dashboard/>} />
          <Route path="/register" element={<Register/>} />
          <Route path="/login" element={<Login />} />
          <Route path="/createprofile" element={<CreateProfile />} />
          <Route path="/message" element={<Message />} />
          <Route path="/mission" element={<Mission/>}/>
        </Routes> 
       </div>
      </div>
  )
}

export default App
