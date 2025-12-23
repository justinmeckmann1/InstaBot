from Utils.Path_helper import validate
from Image.Caption import get_caption_from_file
from API.Upload import upload_to_imgbb

import sys

class Image: 
    def __init__(self):
        self.__path = None
        self.__caption = None
        self.__url = None       
        self.__imgbb_api_key = None
    
    # path: 
    @property
    def path(self): 
        return self.__path
    
    @path.setter
    def path(self, filepath): 
        self.__path = validate(filepath)
    
    # caption    
    @property
    def caption(self):
        if self.__caption is None and self.__path is not None:
            try: self.__caption = get_caption_from_file(self.__path)
            except: sys.exit("Unable to fetch caption from Title and Date.") 
        return self.__caption
    
    @property
    def url(self): 
        return self.__url

    def upload(self, api_key):
        if not self.path: 
            raise("Cannot upload image without a path specified.")
        self.__url = upload_to_imgbb(api_key, self.path, expire_seconds=600) # expires after 5 minuets 
        
    def delete(self): 
        """
        Removes image from used images
        """
        #TODO not implemented yet!
        raise NotImplementedError
    
    def move_on_disK(self, dst):
        dst = validate(dst)
        self.path.replace(dst.joinpath(self.path.name))
        
        print(f"Moved image from {self.path} to {dst.joinpath(self.path.name)}")
