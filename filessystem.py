from os import listdir
from typing import List

class CustomFS:
    def __init__(self):
        self.path = ""
        with open("./basepath.txt") as x:
            for i in x:
                if i.startswith("basepath="):
                    docpath = i.split("=")
                    self.path = docpath[-1]

    def list_all_dirs(self) -> List[str]:
        return listdir(self.path)
    
    def get_path(self):
        return(self.path)
    
