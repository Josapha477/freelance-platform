import React, { useState } from "react";
import api from "../services/client";
import { ACCESS_TOKEN, REFRESH_TOKEN } from "../constant";
import { useNavigate } from "react-router-dom";



interface LoginForm  {
    username: string;
    password: string;
}


const Login = () => {
    const [formData, setFormData] = useState<LoginForm>({
        username: '',
        password: '',
    })
    const navigate = useNavigate()

const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setFormData({
        ...formData,
        [e.target.name]: e.target.value
    })
}

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault()
        try {
            const res = await api.post('api/v1/user/login/',
                { username: formData.username, password: formData.password }
            );
            localStorage.setItem(ACCESS_TOKEN, res.data.access);
            localStorage.setItem(REFRESH_TOKEN, res.data.refresh);
            navigate("/");
        }
        catch (error) {
            alert(error);
        }
        
        
}
    

    return (
        <div className="flex min-h-screen  
        justify-center items-center">
            <div className="">
                <form onSubmit={handleSubmit} className="flex flex-col gap-10 
                  justify-center items-center shadow-2xl">
                    <div>
                        <input type="username" className="input w-100"
                            value={formData.username} name="username"
                            onChange={handleChange}
                            placeholder="username" />
                    </div>
                    <div>
                        <input className="input w-100"
                            type="password"
                            value={formData.password}
                            name="password"
                            onChange={handleChange}
                            placeholder="password"
                        />
                    </div>
                    <div>
                        <button type="submit" className="btn w-100">connecter</button>
                    </div>
                </form>
            </div>
        </div>
    )
}


export default Login
