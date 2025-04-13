# YouTube Video Summarizer 🎥📝

![Preview image](https://github.com/UmeshSamartapu/Forecasting_of_Smart_City_Traffic_Patterns_upskillcampus_Edunet_DSML_Internship/blob/main/templates/Smart%20City%20Traffic%20Forecasting%20pic.png)

## Overview

An AI-powered tool that automatically generates text summaries from YouTube videos using OpenAI's Whisper for speech recognition and Facebook's BART for text summarization.

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
**outputs/audio/:** Downloaded audio files

**outputs/transcripts/:** Full text transcripts

**outputs/summaries/:** Generated summaries

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
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Open Source](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://opensource.org/)


## Demo 
### You can watch the ([youtube video](   )) for demo
<p align="center">
  <img src="    " />
</p>  


## 📫 Let's Connect

[![LinkedIn](https://img.shields.io/badge/-LinkedIn-0077B5?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/umeshsamartapu/)
[![Twitter](https://img.shields.io/badge/-Twitter-1DA1F2?style=flat-square&logo=twitter&logoColor=white)](https://x.com/umeshsamartapu)
[![Email](https://img.shields.io/badge/-Email-D14836?style=flat-square&logo=gmail&logoColor=white)](mailto:umeshsamartapu@gmail.com)
[![Instagram](https://img.shields.io/badge/-Instagram-E4405F?style=flat-square&logo=instagram&logoColor=white)](https://www.instagram.com/umeshsamartapu/)
[![Buy Me a Coffee](https://img.shields.io/badge/-Buy%20Me%20a%20Coffee-FBAD19?style=flat-square&logo=buymeacoffee&logoColor=black)](https://www.buymeacoffee.com/umeshsamartapu)

---


