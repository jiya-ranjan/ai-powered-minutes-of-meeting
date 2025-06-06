# 📝 Meeting Summarizer – AI-Powered Minutes of Meeting Generator

A powerful AI tool that takes an audio file (e.g., meeting recording) as input and produces:
- 🔊 A **transcript** of the meeting using [Whisper.cpp](https://github.com/ggerganov/whisper.cpp)
- ✍️ A **summary** using an LLM from the [Ollama](https://ollama.com/) server
- 📄 A downloadable transcript file

Perfect for generating **Minutes of Meeting (MoM)** with support for multiple Whisper and LLM models.

---

## 🔧 Features

- Upload any audio file (`.mp3`, `.wav`, `.m4a`, etc.)
- Transcribe using **locally installed Whisper models**
- Summarize using **LLMs from Ollama**
- Provide **optional context** to improve summary relevance
- Get a **clear summary** and **downloadable transcript**
- Simple **Gradio web interface**

---

## 🚀 Tech Stack

| Component        | Tools Used                           |
|------------------|--------------------------------------|
| Audio Processing | `ffmpeg`                             |
| Transcription    | `whisper.cpp` (GGML models)          |
| Summarization    | `Ollama` server + LLMs (e.g., llama3, mistral) |
| Interface        | `Gradio`                             |
| Language         | Python 3                             |


