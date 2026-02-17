from pathlib import Path
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from filessystem import CustomFS

app = FastAPI()
cfs = CustomFS()

BASE_PATH = Path(cfs.get_path()).resolve()

@app.get("/files/{file_path:path}")
def get_file(file_path: str):
    full_path = (BASE_PATH / file_path).resolve()

    if not str(full_path).startswith(str(BASE_PATH)):
        raise HTTPException(status_code=403)

    if not full_path.exists():
        raise HTTPException(status_code=404)

    return FileResponse(full_path)