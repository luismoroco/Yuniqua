import { Route, Routes } from 'react-router-dom';

import Login from './pages/Login.jsx';
import SignUp from './pages/SignUp.jsx';
import App from './App.jsx';
import Editor from './pages/Editor.jsx';

function MainRoutes () {
    return(
        <Routes>
            <Route path="/login" element={<Login />}/>
            <Route path="/editor" element={<Editor />}/>
            <Route path="/" element={<SignUp />}/>
        </Routes>
    );
}

export default MainRoutes;