import React, { useState } from 'react';
import './App.css';
import axios from "axios";

function App() {
  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);

  const handleUpload = async () => {
    if (!file) return alert("Please upload a file");

    setLoading(true);

    const formData = new FormData();
    formData.append("file", file);

    try {
      const res = await axios.post("http://localhost:5000/upload", formData, {
        headers: { "Content-Type": "multipart/form-data" },
      });
      setResult(res.data);
    } catch (error) {
      alert("Upload failed, please try again");
      console.error(error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container">
      <h1>AI Meeting Extractor</h1>
      <p className="subtext">
        Upload your meeting audio and get instant transcripts, summaries and action items
      </p>

      <div>
        <input
          type="file"
          accept="audio/*"
          onChange={(e) => setFile(e.target.files[0])}
        />
      </div>

      <button onClick={handleUpload} disabled={loading}>
        {loading ? "Analyzing..." : "Upload & Analyze"}
      </button>

      {loading && <div className="loader"></div>}

      {result && (
        <div className="results">
          <section>
            <h2>AI Summary</h2>
            <pre>{result.analysis}</pre>
          </section>
        </div>
      )}
    </div>
  );
}

export default App;
