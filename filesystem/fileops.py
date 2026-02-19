from pathlib import Path

class FileOps:
    def __init__(self):
        pass

    def get_file_metadata(self, path: Path) -> dict:
        stat = path.stat()

        return {
            "name": path.name,
            "extension": path.suffix,
            "size": stat.st_size,
            "created": stat.st_ctime,
            "modified": stat.st_mtime,
            "type": "directory" if path.is_dir() else "file"
        }
    
    def get_list_files_metadata(self, path: str) -> list:
        result = []
        base_path = Path(path)
        if base_path.is_file():
            return self.get_file_metadata(base_path)
        else:
            for item in base_path.iterdir():
                result.append(self.get_file_metadata(item))

        return result
    
    def rename_file(self, path: str, new_name: str) -> dict:
        base_path = Path(path)
        if not base_path.exists():
            return {"error": "file does not exist"}
        
        old_name = base_path.name
        new_path = base_path.parent / new_name
        base_path.rename(new_path)

        return {
            "oldfilename": old_name,
            "newfilename": new_path.name,
            "newpath": str(new_path)
        }
    
    def delete_file(self, path: str) -> dict:
        file_path = Path(path)
        if not file_path.exists():
            return {"error": "file does not exist"}

        if not file_path.is_file():
            return {"error": "path is not a file"}

        file_path.unlink()

        return {
            "status": "success",
            "deleted": file_path.name,
            "path": str(file_path)
        }




