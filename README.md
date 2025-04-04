# YouTube Video Summarizer 🎥📝

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Open Source](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://opensource.org/)

An AI-powered tool that automatically generates text summaries from YouTube videos using OpenAI's Whisper for speech recognition and Facebook's BART for text summarization.

![Workflow Diagram](https://via.placeholder.com/800x400.png?text=YouTube+Audio+→+Whisper+Transcription+→+BART+Summarization)

## Features ✨

- 🎧 Download audio from YouTube videos
- 🗣️ Transcribe speech to text using Whisper (Base model)
- 📑 Generate concise summaries with BART-Large-CNN
- 💾 Save full transcripts and summaries with metadata
- ⚡ CPU-only operation (No GPU required)

## Project Structure 📂

```bash
youtube-summarizer/
│
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── audio_processor.py
│   └── text_processor.py
│
├── outputs/
│   ├── audio/          # Downloaded audio files
│   ├── transcripts/    # Full text transcripts
│   └── summaries/      # Generated summaries
│
├── assets/             # For README images/diagrams
│   ├── workflow.png
│   └── terminal-demo.gif
│
├── venv/               # Python virtual environment
│
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

## Installation ⚙️

**Prerequisites**: Python 3.8+ and FFmpeg

1. Clone repository:
```bash
git clone https://github.com/UmeshSamartapu/YT_Transcription_without_API.git
cd YT_Transcription_without_API
```
2.Create a Venv
```bash
python -m venv venv
```
3.Enter the virtual environment (Win)
```bash
venv\scripts\activate
```
4.Install dependencies
```bash
pip install -r requirements.txt
```
5.Run the application
```bash
python main.py
```

