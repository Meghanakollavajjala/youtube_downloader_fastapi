# 🎬 YouTube Downloader (FastAPI + GitHub Pages)

This project provides a **YouTube video downloader** using **FastAPI** as the backend and **HTML/JavaScript** frontend. It enables users to:

- 🔍 Fetch available formats for any YouTube video
- 📥 Download video in selected resolution **with audio merged**
- 🎧 Ensure playback compatibility (MP4 format with audio)
- 🌐 Use via browser (CORS enabled) with a simple UI

---

## 🚀 Features

✅ Get YouTube video formats via API  
✅ Download MP4 video with audio using `yt-dlp`  
✅ Backend deployed on **Render**  
✅ Frontend hosted on **GitHub Pages**  
✅ Clean, minimal UI and setup  
✅ Compatible with modern browsers  

---

## 🌐 Live Demo

- 🔗 **Frontend**: [https://meghanakollavajjala.github.io/youtube_downloader_fastapi/index.html](https://meghanakollavajjala.github.io/youtube_downloader_fastapi/index.html)  
- 🔗 **Backend API** (Render): [https://youtube-downloader-fastapi-d3ot.onrender.com](https://youtube-downloader-fastapi-d3ot.onrender.com)

---

## 🛠️ Requirements

- Python 3.7+
- FFmpeg installed and accessible via system PATH
- `yt-dlp` (installed via `requirements.txt`)

---

## ⚙️ Setup Locally

1. **Clone the repo**
   ```bash
   git clone https://github.com/meghanakollavajjala/youtube_downloader_fastapi.git
   cd youtube_downloader_fastapi

2. Install dependencies

   pip install -r requirements.txt

3. Run FastAPI backend

   uvicorn App:app --reload

4. Open frontend
   
   Just open index.html in your browser
   Or deploy using GitHub Pages as you’ve done

