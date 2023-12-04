import { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

function SignUp() {
    const [formValues, setFormValues] = useState({username:"",password:"",alias:""});

    const navigate = useNavigate();

    const handleInputChange = (e) => {
        const { name, value } = e.target;
        setFormValues((prev) => ({
            ...prev,
            [name]: value,
        }));
        console.log(formValues);
    };

    const handleSubmit = (event) => {
        event.preventDefault();

        axios.post("http://127.0.0.1:5000/user", {
            username: formValues.username,
            password: formValues.password,
            alias: formValues.alias
        }).then(function(response){
            alert("usuario creado");
            navigate('/login');
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
                            Register your account
                        </h1>
                        <form className="space-y-4 md:space-y-6" onSubmit={handleSubmit}>
                            <div>
                                <label htmlFor="username" className="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Your user</label>
                                <input
                                    type="text"
                                    name="username"
                                    id="username"
                                    className="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                                    placeholder="user"
                                    required
                                    value = {formValues.username}
                                    onChange={handleInputChange}
                                />
                            </div>
                            <div>
                                <label htmlFor="alias" className="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Alias</label>
                                <input
                                    type="text"
                                    name="alias"
                                    id="alias"
                                    placeholder="alias"
                                    className="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                                    required
                                    value = {formValues.alias}
                                    onChange={handleInputChange}
                                />
                            </div>
                            <div>
                                <label htmlFor="password" className="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Password</label>
                                <input
                                    type="password"
                                    name="password"
                                    id="password"
                                    placeholder="••••••••"
                                    className="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                                    required
                                    value = {formValues.password}
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
                                Already have an account? <a href="/login" className="font-medium text-[#0284c7] hover:underline dark:text-[#075985]">Login here</a>
                            </p>
                        </form>
                    </div>
                </div>
            </div>
        </section>
    )
}

export default SignUp;