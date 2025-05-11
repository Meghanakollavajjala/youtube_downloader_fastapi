from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import yt_dlp
import os

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class VideoRequest(BaseModel):
    url: str

class DownloadRequest(BaseModel):
    url: str
    format_id: str

@app.get("/")
async def root():
    return {"message": "Welcome to the YouTube Downloader API"}

@app.post("/formats")
async def get_formats(request: VideoRequest):
    try:
        with yt_dlp.YoutubeDL() as ydl:
            info = ydl.extract_info(request.url, download=False)
            formats = [
                {
                    "format_id": fmt["format_id"],
                    "resolution": fmt.get("resolution", fmt.get("height", "unknown")),
                    "ext": fmt.get("ext", "unknown"),
                    "audio_channels": fmt.get("audio_channels", "no audio"),
                }
                for fmt in info.get("formats", [])
            ]
            return {"formats": formats}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error getting formats: {str(e)}")

@app.post("/download")
async def download_video(request: DownloadRequest):
    output_file = "downloaded_video.mp4"

    ydl_opts = {
        "format": f"{request.format_id}+bestaudio[ext=m4a]/best",
        "outtmpl": "temp.%(ext)s",
        "merge_output_format": "mp4",
        "postprocessors": [{
            "key": "FFmpegVideoConvertor",
            "preferedformat": "mp4",
        }],
        "quiet": True,
        "noprogress": True,
    }

    try:
        # Remove old files if exist
        if os.path.exists(output_file):
            os.remove(output_file)

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([request.url])

        # Rename to consistent filename if yt-dlp uses temp name
        for file in os.listdir():
            if file.startswith("temp") and file.endswith(".mp4"):
                os.rename(file, output_file)
                break

        if not os.path.exists(output_file):
            raise HTTPException(status_code=404, detail="File not found after download.")

        return FileResponse(output_file, media_type="video/mp4", filename="youtube_video.mp4")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error downloading video: {str(e)}")
