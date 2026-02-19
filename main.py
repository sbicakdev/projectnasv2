from fastapi import FastAPI, Form, File, UploadFile
from core.pnasapi import PnasAPI
from core.jsonmodels.jsonmodels import RenameRequest

app = FastAPI()
api = PnasAPI()

@app.get("/files/{file_path:path}")
def get_files(file_path):
    return api.get_files_json(file_path)

@app.get("/download/{file_path:path}")
def download_file(file_path: str):
    return api.download_file(file_path)

@app.post("/upload/{file_path:path}")
async def upload(file: UploadFile = File(...), relative_path: str = Form("")):   
    return await api.save_upload_file(file, relative_path)

@app.patch("/rename/{file_path:path}")
def rename(file_path: str, request: RenameRequest):
    return api.rename_file(file_path, request.new_name)