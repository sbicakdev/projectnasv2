from pathlib import Path
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from filesystem.fsystem import CustomFS
from core.pnasapi import PnasAPI

app = FastAPI()
pnasapi = PnasAPI()

BASE_PATH = Path(pnasapi.get_BASE_PATH())

@app.get("/files/{file_path:path}")
def get_files(file_path):
    return PnasAPI.get_files_json(file_path)

@app.get("/download/{file_path:path}")
def download_file(file_path: str):
    full_path = (BASE_PATH / file_path).resolve()

    if not full_path.exists():
        raise HTTPException(status_code=404, detail="File not found")

    if not full_path.is_file():
        raise HTTPException(status_code=400, detail="Not a file")

    return FileResponse(
        path=full_path,
        filename=full_path.name,
        media_type="application/octet-stream"
    )
