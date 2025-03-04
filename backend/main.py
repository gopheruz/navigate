from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import os
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

AUDIO_DIR = "./files"

@app.get("/tracks")
def get_tracks():
    tracks = os.listdir(AUDIO_DIR)
    return {"tracks": sorted(tracks)}

@app.get("/track/{filename}")
def get_track(filename: str):
    file_path = os.path.join(AUDIO_DIR, filename)
    if os.path.exists(file_path):
        return FileResponse(file_path, media_type="audio/mp3")
    return {"error": "File not found"}
