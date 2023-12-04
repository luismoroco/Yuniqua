import { Route, Routes } from 'react-router-dom';

import Login from './pages/Login.jsx';
import SignUp from './pages/SignUp.jsx';
import Editor from './pages/Editor.jsx';
import CodeEditor from "./components/CodeEditor.jsx";

function MainRoutes () {
    return(
        <Routes>
            <Route path={"/editor"} element={<CodeEditor/>}/>
        </Routes>
    );
}

export default MainRoutes;