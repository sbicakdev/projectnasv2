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




