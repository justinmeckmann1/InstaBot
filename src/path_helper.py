from pathlib import Path 

def validate(path_or_dir) -> Path:
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
            print("Not a valid directory")
            exit()
    
    # confirm dir exists: 
    if not path_or_dir.exists(): 
        print(f"Directory {path_or_dir} does not exist.")
        exit()
        
    return path_or_dir