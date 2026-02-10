# YouTube Video QA Bot

An interactive Python CLI tool that allows you to ask questions about any YouTube video. It extracts transcripts, chunks them, generates embeddings, and performs retrieval-augmented QA using a local LLM.

![YouTube QA Screenshot](youtube%20QA.PNG)

## Features

- Fetches YouTube video transcripts (auto-generated or uploaded)
- Processes and formats transcripts
- Splits transcripts into overlapping chunks
- Generates embeddings using `all-MiniLM-L6-v2`
- Stores embeddings in FAISS for fast retrieval
- Interactive CLI for asking multiple questions per video
- Supports switching between videos seamlessly
- Uses a local LLM (e.g., Ollama or LLaMA2) for RAG-style answers

## Installation

```bash
git clone <your-repo-url>
cd "youtube video QA bot"
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
