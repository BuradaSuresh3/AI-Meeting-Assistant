# AI Meeting Assistant

## Overview

AI Meeting Assistant is an AI-powered application that converts meeting recordings into structured meeting summaries.

The application uses Whisper for speech-to-text transcription and Llama3 (via Ollama) for intelligent meeting analysis.

## Features

* Upload audio recordings
* Automatic speech-to-text transcription
* AI-generated meeting summaries
* Key decisions extraction
* Action items generation
* Challenges identification
* Next steps generation
* Download summary as text file

## Tech Stack

* Python
* Streamlit
* OpenAI Whisper
* Ollama
* Llama3
* FFmpeg

## Workflow

Audio File → Whisper → Transcript → Llama3 → Meeting Summary

## Installation

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Install Ollama

Download and install Ollama.

### 3. Pull Llama3 model

```bash
ollama pull llama3
```

### 4. Run the application

```bash
streamlit run frontend/app.py
```

## Project Structure

```text
AI-Meeting-Assistant/
│
├── backend/
├── frontend/
├── README.md
├── requirements.txt
└── .gitignore
```

## Future Improvements

* PDF export
* Speaker identification
* Telugu to English translation
* Meeting history
* Cloud deployment

## Author

Burada Suresh
