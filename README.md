# 🎬 YouTube Downloader API (FastAPI)

This project provides a simple REST API built with **FastAPI** and **yt-dlp** that allows users to:

- 🔍 Fetch available formats for a YouTube video
- 📥 Download a video in selected resolution with merged audio
- 🎧 Ensure playback compatibility (MP4 + audio)

---

## 🚀 Features

- Fetch YouTube video formats via POST
- Download MP4 video with audio (using `yt-dlp` and `ffmpeg`)
- CORS enabled (usable from web frontends)
- Minimal and production-friendly setup

---

## 🛠️ Requirements

- Python 3.7+
- FFmpeg installed and accessible from PATH
- yt-dlp (auto-installed via `requirements.txt`)

---

## 📦 Setup

```bash
git clone https://github.com/yourusername/youtube-downloader-fastapi.git
cd youtube-downloader-fastapi
pip install -r requirements.txt
