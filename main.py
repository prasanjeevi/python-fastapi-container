from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/api/greet")
def greet():
    return {"message": "Hello World"}

@app.get("/api/download")
async def download(file: str):
    media_type = 'application/octet-stream'
    if file.lower().endswith('xlsx'):
      media_type = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    elif file.lower().endswith('pptx'):
      media_type = 'application/vnd.openxmlformats-officedocument.presentationml.presentation'
    return FileResponse(path='downloads/'+file, filename=file, media_type=media_type)