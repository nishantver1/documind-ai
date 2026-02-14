import { useState } from "react";
import "./App.css";

function App() {
  const [file, setFile] = useState(null);
  const [chat, setChat] = useState([]);
  const [question, setQuestion] = useState("");
  const [loading, setLoading] = useState(false);

  // upload document
  const uploadFile = async () => {
    if (!file) return alert("Select PDF first");

    const formData = new FormData();
    formData.append("file", file);

    setLoading(true);

    await fetch("http://127.0.0.1:5000/upload", {
      method: "POST",
      body: formData,
    });

    setLoading(false);
    alert("Document uploaded & ready!");
  };

  // send message
  const sendMessage = async () => {
    if (!question) return;

    const userMsg = { type: "user", text: question };
    setChat((prev) => [...prev, userMsg]);
    setQuestion("");
    setLoading(true);

    const res = await fetch("http://127.0.0.1:5000/ask", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ question }),
    });

    const data = await res.json();

    const botMsg = { type: "bot", text: data.answer };
    setChat((prev) => [...prev, botMsg]);

    setLoading(false);
  };

  return (
    <div className="app">
      {/* Sidebar */}
      <div className="sidebar">
        <h2>📄 DocuMind AI</h2>

        <input type="file" onChange={(e) => setFile(e.target.files[0])} />
        <button onClick={uploadFile}>Upload PDF</button>

        <div className="tips">
          <p>- Image support with OCR</p>
          <p>- Multiple pdf support</p>
          <p>- Try asking:</p>
          <small>• Summarize document</small>
          <small>• Explain topic</small>
          <small>• Generate MCQs</small>
          <small>• Teach me simply</small>
        </div>
      </div>

      {/* Chat section */}
      <div className="chatSection">
        <div className="chatHeader">AI Document Assistant</div>

        <div className="chatBox">
          {chat.map((msg, i) => (
            <div key={i} className={msg.type}>
              {msg.text}
            </div>
          ))}
          {loading && <div className="bot">Thinking...</div>}
        </div>

        <div className="inputArea">
          <input
            value={question}
            onChange={(e) => setQuestion(e.target.value)}
            onKeyDown={(e)=>{
              if(e.key ==="Enter"){
                sendMessage();
              }
            }}
            placeholder="Ask anything from your document..."
          />
          <button onClick={sendMessage}>Send</button>
        </div>
      </div>
       {/* RIGHT SIDEBAR */}
    <div className="rightbar">
      <h3>Project Info</h3>

      <div className="card">
        <b>Model:</b>
        <br />
        <small>Mistral (local)</small>
      </div>

      <div className="card">
        <b>Vector DB:</b>
        <br />
        <small>FAISS semantic search</small>
      </div>

      
    </div>
    </div>
  );
}

export default App;
