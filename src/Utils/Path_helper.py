from pathlib import Path 
import os

def validate(path_or_dir, gen_dir=False) -> Path:
    """
    Args:
        path_or_dir (str or path): string or path pointing to a file or directory

    Returns:
        validated type path variable 
    """
    
    # check if type path, if not change to type path
    if not type(path_or_dir) == Path: 
        try: 
            path_or_dir = Path(path_or_dir)
        except TypeError: 
            raise("Not a valid directory")
    
    # confirm dir exists: 
    if not path_or_dir.exists(): 
        print(f"Directory {path_or_dir} does not exist.")
        
        if gen_dir and path_or_dir.is_dir(): 
            os.makedirs(path_or_dir)
        else:
            raise()        
    return path_or_dir


