from typing import Union

from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from fastapi.staticfiles import StaticFiles
from asciiGenerate import generate_himatika_ascii, generate_bird_ascii
app = FastAPI()
static_file = StaticFiles(directory="assets")
app.mount("/assets",static_file,name= "static")
@app.get("/")
async def home():
    frame = open("assets/txt/logo_himatika/logo.txt","r").read()
    return StreamingResponse(generate_himatika_ascii(frame),media_type="text/plain")


@app.get("/bird")
async def bird():
    list_dir = [open(f"assets/txt/bird_frames/frames{i+1}.txt","r").read() for i in range(27)]
    return StreamingResponse(generate_bird_ascii(list_dir),media_type="text/plain")