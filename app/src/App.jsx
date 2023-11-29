import { useState, useEffect } from 'react'
import io from 'socket.io-client';
import './App.css'

const socket = io("http://127.0.0.1:5000");

function App() {
  const [editorContent, setEditorContent] = useState("")

  useEffect(() => {
    socket.on("message", (newEditorContent) => {
      setEditorContent(newEditorContent);
    })
  }, [])

  const updateEditorContent = () => {
    socket.emit("message", editorContent);
  }

  return (
    <>
      <h1>Vite + React</h1>
      <div className="card">
        <p>
          <input 
            type={"text"}
            value={editorContent}
            onChange={(e) => setEditorContent(e.target.value)}
          />
        </p>
      </div>
      <button
        onClick={updateEditorContent}
      > Run </button>
    </>
  )
}

export default App
