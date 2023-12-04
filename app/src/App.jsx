import React, { useState} from 'react';
import {Router, Route, Navigate } from 'react-router-dom';
import Login from './components/SingIn';
import CodeEditor from './components/CodeEditor';

function App() {
  // const [isAuthenticated, setAuthenticated] = useState(false);

  return (
  <CodeEditor
    language={'python'}
    tittle={'Editor python'}
  />
  );
}

{/* <>
      <h1>Code Editor Online</h1>
      <CodeEditor
        language={'python'}
      />
      <button id='run-code'
        onDoubleClick={console.log('xd clickeaste')}
      > Run </button>
    </> */}

export default App;