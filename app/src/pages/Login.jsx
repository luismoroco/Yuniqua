import { useEffect, useState } from 'react'
import axios from 'axios';
import httpClient from "../httpClient.js";
import { useNavigate } from 'react-router-dom';
import { useLocation} from "react-router-dom";

function Login() {

    const [formValues, setFormValues] = useState({username:"",password:""});

    const navigate = useNavigate();
    const location = useLocation()
    const handleInputChange = (e) => {
        const { name, value } = e.target;
        setFormValues((prev) => ({
            ...prev,
            [name]: value,
        }));
    };

    const handleSubmit = (event) => {
        event.preventDefault();

        httpClient.post("http://127.0.0.1:5000/auth/log-in",{
            username: formValues.username,
            password: formValues.password
        }).then(function(response){
            navigate("/editor", {state: {data: response.data.data}});
        });
    };


    return (
        <section className="min-h-screen bg-gray-50 dark:bg-gray-900 items-center justify-center">
            <div className="flex flex-col items-center justify-center px-6 py-8 mx-auto md:h-screen lg:py-0">
                <h2 className="flex items-center mb-6 text-2xl font-semibold text-gray-900 dark:text-white">
                    Yuniqua
                </h2>
                <div className="w-full bg-white rounded-lg shadow dark:border md:mt-0 sm:max-w-md xl:p-0 dark:bg-gray-800 dark:border-gray-700">
                    <div className="p-6 space-y-4 md:space-y-6 sm:p-8">
                        <h1 className="text-xl font-bold leading-tight tracking-tight text-gray-900 md:text-2xl dark:text-white">
                            Sign in to your account
                        </h1>
                        <form className="space-y-4 md:space-y-6" onSubmit={handleSubmit}>
                            <div>
                                <label htmlFor="username" className="block mb-2 text-sm font-medium text-gray-900 dark:text-white text-start">Your user</label>
                                <input
                                    type="text"
                                    name="username"
                                    id="username"
                                    value = {formValues.username}
                                    className="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                                    placeholder="user"
                                    required
                                    onChange={handleInputChange}
                                />
                            </div>
                            <div>
                                <label htmlFor="password" className="block mb-2 text-sm font-medium text-gray-900 dark:text-white text-start">Password</label>
                                <input
                                    type="password"
                                    name="password"
                                    id="password"
                                    placeholder="••••••••"
                                    className="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                                    value = {formValues.password}
                                    required
                                    onChange={handleInputChange}
                                />
                            </div>
                            <button
                                type="submit"
                                className="w-full text-white bg-[#0284c7] hover:bg-[#075985] focus:ring-4 focus:outline-none focus:ring-[#38bdf8] font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-[#0284c7] dark:hover:bg-bg-[#075985] dark:focus:ring-[#38bdf8] "
                            >
                                Sign in
                            </button>
                            <p className="text-sm font-light text-gray-500 dark:text-gray-400">
                                Don’t have an account yet? <a href="/signup" className="font-medium text-[#0284c7] hover:underline dark:text-[#075985]">Sign up</a>
                            </p>
                        </form>
                    </div>
                </div>
            </div>
        </section>
    )
}

export default Login;