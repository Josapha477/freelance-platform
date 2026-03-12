import React, { useState } from "react";
import api from "../services/client";


interface RegisterData {
    first_name: string;
    last_name: string;
    username: string;
    password: string;
}


const Register = () => {
    const [formData, setFormData] = useState<RegisterData>({
        first_name: "",
        last_name: "",
        username: '',
        password: '',
    });

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault()

    }

    const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => (
        setFormData({
            ...formData,
            [e.target.name]: e.target.value
        })
    )


    return (
        <div className='flex flex-col min-h-screen 
                md:flex-row   items-center justify-center'>
            <div className="hidden md:flex md:w-full 
            bg-gradient-to-br from-blue-600 p-8 to-gray-500 rounded">
                <div className="flex flex-col justify-center 
                    text-white max-w-md mx-auto">
                    <h1 className="text-4xl font-bold mb-6">
                        Rejoignez la plus grande communaute de freelance
                    </h1>
                    <ul className="space-y-4 mb-8">
                        <li className="flex items-center">
                            <i className="fas fa-check-circle mr-3"></i>
                            <span>Accedez a des milliers de projets</span>
                        </li>
                        <li className="flex items-center">
                            <i className="fas fa-check-circle mr-3"></i>
                            <span>Construisez votre portfolio</span>
                        </li>
                        <li className="flex items-center">
                            <i className="fas fa-check-circle mr-3"></i>
                            <span>Recevez des paiements securises</span>
                        </li>
                        <li className="flex items-center">
                            <i className="fas fa-check-circle mr-3"></i>
                            <span>Travaillez en toute flexibilitee</span>
                        </li>
                    </ul>
                    <div className="flex flex-col gap-3 bg-white/10 backdrop-blur-sm rounded-lg p-6">
                        <div className="flex w-10 h-10 rounded-full text-center
                         bg-green-200 justfiy-center items-center">
                            <h1 className="text-center">SR</h1>
                        </div>
                        <p className="italic">Cette platform a transformee ma carriere freelance !</p>
                        <p className="mt-2 font-semi-bold">Sarah, Developpeuse Web</p>
                    </div>
                </div>
            </div>
            <div className="w-full md:w-full flex items-center justify-center p-4 md:p-8">
                <div className="w-full max-w-md">
                    <div className="text-center mb-8">
                        <div className="flex justify-center md:hidden mb-4">
                            <div className="h-12 w-12 bg-blue-600 rounded-lg 
                            flex items-center justify-center">
                                <span className="text-white font-bold text-xl">
                                    F
                                </span>
                            </div>
                            <h2 className="text-3xl font-bold text-gray-800">Creer un compte</h2>
                            <p className="text-gray-600 mt-2">Rejoignez notre plateforme en moins de 2 minutes</p>
                        </div>
                        <form className="bg-white rounded-2xl shadow-lg p-6 md:p-8">
                            <div className="mb-6">
                                <label className="block text-gray-700 mb-3 font-medium">Je suis :</label>
                                <div className="grid grid-cols-2 gap-4">
                                    <button className="btn ">
                                        <i className="fas fa-user-tie mr-2"></i>
                                        Freelance
                                    </button>
                                    <button className="btn">
                                        <i className="fas fa-briefcase mr-2"></i>
                                        Client
                                    </button>
                                </div>
                            </div>
                            <div className="space-y-4">
                                <div>
                                    <label htmlFor="fullName" className="block text-gray-700 mb-2 font-medium">
                                        Nom Complet <span className="text-red-500">*</span>
                                    </label>
                                    <div className="relative">
                                        <i className="fas fa-user absolute left-3 top-3 text-gray-400"></i>
                                        <input type="text" id="fullName" required
                                            className="input"
                                            placeholder="Votre Nom complet"
                                        />
                                    </div>
                                </div>

                                <div>
                                    <label htmlFor="username" className="block text-gray-700 mb-2 font-medium">
                                        Username <span className="text-red-500">*</span>
                                    </label>
                                    <div className="relative">
                                        <i className="fas fa-user absolute left-3 top-3 text-gray-400"></i>
                                        <input type="text" id="username" required
                                            className="input"
                                            placeholder="Votre username"
                                        />
                                    </div>
                                </div>

                                <div>
                                    <label htmlFor="password" className="block text-gray-700 mb-2 font-medium">
                                        Mot de passe <span className="text-red-500">*</span>
                                    </label>
                                    <div className="relative">
                                        <i className="fas fa-lock absolute left-3 top-3 text-gray-400"></i>
                                        <input type="password" id="password" required
                                            className="input"
                                            placeholder="......"
                                        />
                                        <button type="button" className="absolute right-3 top-3 
                                            text-gray-400 hover:text-gray-600">
                                                <i className="fas fa-eye"></i>
                                        </button>
                                        <p>8 caracteres minimum avec majuscule, minuscule et chiffre</p>
                                    </div>
                                    <div id="freelanceFields" className="space-y-4">
                                        <div>
                                            <label htmlFor="specialty" className="block text-gray-700 mb-2 font-medium">
                                                Competences <span className="text-red-500">*</span>
                                            </label>
                                            <select name="competence" id="specialty">
                                                <option value="">Competences disponible</option>
                                                <option value="choices">GHOICES</option>
                                            </select>
                                        </div>

                                        <div>

                                        </div>
                                    </div>
                                </div>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    )
}


export default Register