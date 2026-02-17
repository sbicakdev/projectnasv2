from pathlib import Path
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from filesystem.fsystem import CustomFS
from core.pnasapi import PnasAPI

app = FastAPI()
pnasapi = PnasAPI()

BASE_PATH = Path(pnasapi.get_BASE_PATH())

@app.get("/{file_path:path}")
def get_files(file_path):
    return PnasAPI.get_files_json(file_path)
