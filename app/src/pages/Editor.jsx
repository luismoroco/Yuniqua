import { useState, useEffect } from 'react';
import axios from 'axios';
import httpClient from '../httpClient.js'

function Editor(){
    const [userID,setUserID] = useState("");
    const [userName,setUserName] = useState("");
    const [showModal, setShowModal] = useState(false);
    const [contentModal, setContentModal] = useState({edname:"",max_connections:"",language:""});
    const [editorsList, setEditorsList] = useState([]);
    const [hasEditors, setHasEditors] = useState((false));

    const handleInputChange = (e) => {
        const { name, value } = e.target;
        setContentModal((prev) => ({
            ...prev,
            [name]: value,
        }));
    };


    const handleSubmitModal = (event) => {
        event.preventDefault();

        axios.post("http://127.0.0.1:5000/editor", {
            name: contentModal.edname,
            max_connections: contentModal.max_connections,
            language: contentModal.language
        }).then(function(response){
            alert("Editor created");
            setShowModal(false);
        });
    };

    const path = "http://127.0.0.1:5000/auth/test"
    useEffect(() => {
        httpClient.get(path).then(res => {
            setUserID(res.data.user_id);
            setUserName(res.data.userName);
        })
    }, [path]);

    const path1 = `http://127.0.0.1:5000/editor/1/room`
    useEffect(()=>{
        axios.get(path1).then(res =>{
            setEditorsList(res.data.split(','));
            setHasEditors(true);
        })

    },[path1])


    return (
        <section className="min-h-screen bg-gray-50 dark:bg-gray-900 items-center justify-center">
            <div className="flex flex-col items-center justify-center px-6 py-8 mx-auto md:h-screen lg:py-0">
                <h2 className="flex items-center mb-6 text-2xl font-semibold text-gray-900 dark:text-white">
                    Yuniqua
                </h2>
                <div className="w-full bg-white rounded-lg shadow dark:border md:mt-0 sm:max-w-md xl:p-0 dark:bg-gray-800 dark:border-gray-700">
                    <div className="p-6 space-y-4 md:space-y-6 sm:p-8">
                        <h1 className="text-xl font-bold leading-tight tracking-tight text-gray-900 md:text-2xl dark:text-white">
                            Hola, {userName} {userID}
                        </h1>

                            <div className="flex flex-row mb-2 text-sm font-medium text-gray-900 dark:text-white space-x-4">
                                <h1 className="text-2xl">Editor</h1>
                                <button
                                    className="block text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
                                    type="button"
                                    onClick={() => setShowModal(true)}
                                >+</button>

                                {showModal ? (
                                <>
                                    <div
                                        className="justify-center items-center flex overflow-x-hidden overflow-y-auto fixed inset-0 z-50 outline-none focus:outline-none"
                                    >
                                        <div className="relative my-6 mx-auto">
                                            {/*content*/}
                                            <div className="border-0 bg-white rounded-lg shadow dark:border relative flex flex-col  outline-none focus:outline-none dark:bg-gray-800 dark:border-gray-700">
                                                {/*header*/}
                                                <div className="flex items-start justify-between p-5 border-b border-solid border-blueGray-200 rounded-t">
                                                    <h3 className="text-3xl font-semibold">
                                                        Create editor
                                                    </h3>
                                                    <button
                                                        className="p-1 ml-auto bg-transparent border-0 text-black opacity-5 float-right text-3xl leading-none font-semibold outline-none focus:outline-none"
                                                        onClick={() => setShowModal(false)}
                                                    >
                                                        <span className="bg-transparent text-black opacity-5 h-6 w-6 text-2xl block outline-none focus:outline-none">
                                                          ×
                                                        </span>
                                                    </button>
                                                </div>
                                                {/*body*/}
                                                <div className="w-full bg-white rounded-lg shadow dark:border md:mt-0 sm:max-w-md xl:p-0 dark:bg-gray-800 dark:border-gray-700">
                                                    <div className="p-6 space-y-4 md:space-y-6 sm:p-8">
                                                        <form className="space-y-4 md:space-y-6" onSubmit={handleSubmitModal}>
                                                            <div>
                                                                <label htmlFor="edname" className="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Name of the editor</label>
                                                                <input
                                                                    type="text"
                                                                    name="edname"
                                                                    id="edname"
                                                                    className="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                                                                    placeholder="name"
                                                                    required
                                                                    value = {contentModal.edname}
                                                                    onChange={handleInputChange}
                                                                />
                                                            </div>
                                                            <div>
                                                                <label htmlFor="max_connections" className="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Number of Connections</label>
                                                                <input
                                                                    type="number"
                                                                    name="max_connections"
                                                                    id="max_connections"
                                                                    placeholder="1"
                                                                    className="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                                                                    required
                                                                    value = {contentModal.max_connections}
                                                                    onChange={handleInputChange}
                                                                />
                                                            </div>
                                                            <div>
                                                                <label htmlFor="language" className="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Language</label>
                                                                <input
                                                                    type="text"
                                                                    name="language"
                                                                    id="language"
                                                                    className="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                                                                    placeholder="CPP, Javascript or Python"
                                                                    required
                                                                    value = {contentModal.language}
                                                                    onChange={handleInputChange}
                                                                />
                                                            </div>

                                                            <button
                                                                type="submit"
                                                                className="w-full text-white bg-[#0284c7] hover:bg-[#075985] focus:ring-4 focus:outline-none focus:ring-[#38bdf8] font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-[#0284c7] dark:hover:bg-bg-[#075985] dark:focus:ring-[#38bdf8] "
                                                            >
                                                                Create
                                                            </button>
                                                        </form>
                                                    </div>
                                                </div>
                                                {/*footer*/}
                                                <div className="flex items-center justify-end p-6 border-t border-solid border-blueGray-200 rounded-b">
                                                    <button
                                                        className="text-red-500 background-transparent font-bold uppercase px-6 py-2 text-sm outline-none focus:outline-none mr-1 mb-1 ease-linear transition-all duration-150"
                                                        type="button"
                                                        onClick={() => setShowModal(false)}
                                                    >
                                                        Close
                                                    </button>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    <div className="opacity-25 fixed inset-0 z-40 bg-black"></div>
                                </>
                            ) : null}

                            </div>

                            <div className="items-center justify-start p-4 w-full">
                                <div className="bg-white rounded-lg shadow dark:bg-gray-700">
                                    {
                                        hasEditors ? (
                                        <div className="p-4 md:p-5">
                                            <ul className="space-y-4 mb-4">
                                                {
                                                    editorsList.map(it => (
                                                        <li>
                                                            <input type="radio" id={it.id} name={it.id} value={it.id} className="hidden peer" required />
                                                            <label htmlFor={it.id} className="inline-flex items-center justify-between w-full p-5 text-gray-900 bg-white border border-gray-200 rounded-lg cursor-pointer dark:hover:text-gray-300 dark:border-gray-500 dark:peer-checked:text-blue-500 peer-checked:border-blue-600 peer-checked:text-blue-600 hover:text-gray-900 hover:bg-gray-100 dark:text-white dark:bg-gray-600 dark:hover:bg-gray-500">
                                                                <div className="block">
                                                                    <div className="w-full text-2xl font-semibold">{it.name}</div>
                                                                    <div className="w-full text-gray-500 dark:text-gray-400">{it.max_connections}</div>
                                                                    <div className="w-full text-gray-500 dark:text-gray-400">{it.language}</div>
                                                                </div>
                                                            </label>
                                                        </li>
                                                    ))
                                                }
                                            </ul>
                                        </div>
                                        ) : null
                                    }
                                </div>
                            </div>

                            <button
                                type="submit"
                                className="w-full text-white bg-[#0284c7] hover:bg-[#075985] focus:ring-4 focus:outline-none focus:ring-[#38bdf8] font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-[#0284c7] dark:hover:bg-bg-[#075985] dark:focus:ring-[#38bdf8] "
                            >
                                next
                            </button>
                    </div>
                </div>
            </div>
        </section>
    )
}

export default Editor;