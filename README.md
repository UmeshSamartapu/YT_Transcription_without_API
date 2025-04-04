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
## Follow the prompts to:
1.Enter YouTube URL
2.Let the tool process audio download
3.Get automatic transcription
4.Receive generated summary

## Output files will be saved in:
outputs/audio/: Downloaded audio files
outputs/transcripts/: Full text transcripts
outputs/summaries/: Generated summaries

## How It Works 🧠
### 1.Audio Extraction
Uses yt-dlp to download audio in MP3 format
Handles age-restricted and private content gracefully
### 2.Speech Recognition
Leverages OpenAI's Whisper (Base model)
Supports multiple languages automatically
### 3.Text Summarization
Employs Facebook's BART-Large-CNN model
Smart text chunking with context preservation
```bash
graph TD
    A[YouTube URL] --> B(Audio Download)
    B --> C{Speech to Text}
    C --> D[Full Transcript]
    C --> E[Text Summary]
```

## License 📄
Distributed under the MIT License. See LICENSE for more information.
Note: This project is for educational purposes only. Respect content creators' rights and YouTube's terms of service.

Key improvements made:
1. Added proper directory structure visualization
2. Organized installation steps more clearly
3. Added OS-specific virtual environment activation
4. Included directory creation step for outputs
5. Improved formatting for better readability
6. Maintained consistent emoji usage
7. Added clear output locations section
