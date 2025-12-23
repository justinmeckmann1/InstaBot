from Utils.Path_helper import validate
from pathlib import Path 

import random
import time

def get_sample(directory: Path, filetypes = ["JPEG","JPG"]):   
    directory = validate(directory)
    
    # parse files
    files = [
        f for f in directory.iterdir()
        if f.as_posix().lower().endswith(tuple(f".{ft.lower()}" for ft in filetypes))
    ]
    
    if len(files) == 0: 
        raise("There are no images in the post directory.")
    
    # return random file
    return random.choice(files)