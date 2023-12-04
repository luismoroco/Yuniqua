import React, { useState, useEffect, useCallback } from 'react';
import Editor from '@monaco-editor/react';
import io from 'socket.io-client';
import axios from 'axios';
import './CodeEditor.css'
import logo_python from '../assets/python.png'
import logo_js from '../assets/js.png'
import logo_cpp from '../assets/cpp.png'
import run from '../assets/run.png'


const socket = io("http://127.0.0.1:8000");

function CodeEditor({language, tittle}) {
  let defaultComment = "";
  let urlImage = logo_python;
  switch (language) {
    case "python":
      defaultComment = "#Welcome to python\n\n";
      urlImage = logo_python;
      break;
    case "cpp":
      defaultComment = "// Welcome to C++\n\n"
      urlImage = logo_cpp;
      break;
    case "javascript":
      defaultComment = "// Welcome to JS!\n\n"
      urlImage = logo_js;
      break;
    default:
      defaultComment = "Unkown Language\n\n"
      break;
  }

  const [editorContent, setEditorContent] = useState("");
  const [apiResponse, setApiResponse] = useState('');

  const handleEditorChange = useCallback((newContent) => {
    setEditorContent(newContent);
    socket.emit('message', newContent);
  }, []);

  const apiUrl = 'http://127.0.0.1:8000/execute/python'
  const handleApiCompilerRequest = async () => {
    try {
      const response = await axios.post(apiUrl, {
        code: editorContent
      });
      console.log(response.data);
      if(response.data.message === 'OK'){
        setApiResponse(response.data.data);
      }else{
        setApiResponse("An Error Ocurred")
      }
      
    } catch (error) {
      console.error('Error al hacer la solicitud a la API:', error);
    }
  };

  useEffect(() => {
    const handleMessage = (newContent) => {
      if (newContent !== editorContent) {
        handleEditorChange(newContent);
      }
    };

    socket.on("message", handleMessage);

    console.log(editorContent);
    return () => {
      socket.off("message", handleMessage);
    };

  }, [editorContent, handleEditorChange]);
  return (
    <>
    <div class="title">{tittle}</div>
    <div class="image-container">
      <img src={urlImage} />
    </div>
    <div class='button-run'>
      <button
        onClick={() => handleApiCompilerRequest()}
      >
        <img src={run} />
      </button>
    </div>
    <br/>
    <div className="contenedor">
      <div className="componente">
        <Editor
          theme='vs-dark'
          height="80vh"
          defaultLanguage= {language}
          defaultValue={defaultComment}
          value={editorContent}
          options={{
            fontSize: 20,
          }}
          onChange={handleEditorChange}
        />
      </div>
      <div className="componente">
        <label className='editor'>Respuesta de la API:</label>
        <div className='editor'>{apiResponse}</div>
      </div>
    </div>
    </>
    

  );
}

export default CodeEditor;