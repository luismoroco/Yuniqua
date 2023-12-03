import { useState, useEffect, useCallback} from 'react'
import io from 'socket.io-client';
import MonacoEditor from 'react-monaco-editor';
import './App.css'

const socket = io("http://127.0.0.1:8000");
// (globalThis).MonacoEnvironment = {
//     getWorkerUrl: function (_moduleId) {
//       return `data:text/javascript;charset=utf-8,${encodeURIComponent(`
//         self.MonacoEnvironment = {
//           baseUrl: 'https://cdn.jsdelivr.net/npm/monaco-editor@latest/min/'
//         };
//         importScripts('https://cdn.jsdelivr.net/npm/monaco-editor@latest/min/vs/base/worker/workerMain.js');
//       `)}`;
//     },
//   };


function App() {
  const [editorContent, setEditorContent] = useState("");

  const handleEditorChange = useCallback((newContent) => {
    // if (newContent !== editorContent) {
      setEditorContent(newContent);
    // }
    socket.emit('message', newContent);
  }, []);

  useEffect(() => {
    // Recuperar el contenido del editor almacenado localmente al cargar la página
    // const storedContent = localStorage.getItem('editorContent');
    // if (storedContent) {
    //   setEditorContent(storedContent);
    // }

    const handleMessage = (newContent) => {
      if (newContent !== editorContent) {
        handleEditorChange(newContent);
      }
    };

    socket.on("message", handleMessage);

    return () => {
      socket.off("message", handleMessage);
    };
  }, [editorContent, handleEditorChange]);

  const options = {
    automaticLayout: true,
    language: 'python'
  }

  return (
    <>
      <h1>Code Editor Online</h1>
      <div className="card">
        <MonacoEditor
          width="800"
          height="600"
          // language="python"
          theme="vs-dark"
          options={options}
          value={editorContent}
          onChange={handleEditorChange}
        />
      </div>
      <button id='run-code'
        // onClick={console.log('xd clickeaste')}
      > Run </button>
    </>
  )
}

export default App
