import React, { useState} from 'react';
import {Router, Route, Navigate } from 'react-router-dom';
import Login from './components/SingIn';
import CodeEditor from './components/CodeEditor';

function App() {
  return (
  <CodeEditor
    language={'python'}
    tittle={'Editor python'}
  />
  );
}

export default App;