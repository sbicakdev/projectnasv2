from filesystem.fileops import FileOps
from filesystem.fsystem import CustomFS
from pathlib import Path

cfs = CustomFS()
BASE_PATH = Path(cfs.get_path()).resolve()

fo = FileOps()

class PnasAPI():
    def __init__(self):
        self.path = BASE_PATH

    def get_files_json(files_path: str):
        full_path = (BASE_PATH / files_path).resolve()
        return {
            "status": "success",
            "path": full_path,
            "files": fo.get_list_files_metadata(full_path)
        }
    
    def get_BASE_PATH(self):
        return self.path