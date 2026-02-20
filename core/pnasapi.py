from fastapi.responses import FileResponse
from filesystem.fileops import FileOps
from filesystem.fsystem import CustomFS
from pathlib import Path
from fastapi import HTTPException, UploadFile

cfs = CustomFS()
BASE_PATH = Path(cfs.get_path()).resolve()

fo = FileOps()


class PnasAPI:

    def __init__(self):
        self.base_path = BASE_PATH

    def get_BASE_PATH(self):
        return self.base_path
    
    def get_safe_path(self, relative_path: str) -> Path:
        full_path = (self.base_path / relative_path).resolve()

        if not str(full_path).startswith(str(self.base_path)):
            raise Exception("Access denied")

        return full_path
    
    def get_files_json(self, files_path: str = "") -> dict:
        full_path = self.get_safe_path(files_path)

        return {
            "status": "success",
            "path": str(full_path),
            "files": fo.get_list_files_metadata(full_path)
        }
    
    def download_file(self, files_path: str = "") -> dict:
            full_path = self.get_safe_path(files_path)

            if not full_path.exists():
                raise HTTPException(status_code=404, detail="File not found")

            if not full_path.is_file():
                raise HTTPException(status_code=400, detail="Not a file")

            return FileResponse(
                path=full_path,
                filename=full_path.name,
                media_type="application/octet-stream"
            )

    async def save_upload_file(self, upload_file: UploadFile, relative_path: str = "") -> dict:

        target_dir = self.get_safe_path(relative_path)

        target_dir.mkdir(parents=True, exist_ok=True)

        file_path = target_dir / upload_file.filename

        with open(file_path, "wb") as f:
            while chunk := await upload_file.read(1024 * 1024):
                f.write(chunk)

        return {
            "name": upload_file.filename,
            "path": str(file_path),
            "size": file_path.stat().st_size
        }
    
    def rename_file(self, relative_path: str, new_file_name: str):
        full_path = self.get_safe_path(relative_path)
        return fo.rename_file(full_path, new_file_name)

    def delete_file(self, relative_path: str = ""):
        full_path = self.get_safe_path(relative_path)
        print(relative_path)
        return fo.delete_file(full_path)