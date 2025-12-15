from Utils.Path_helper import validate
from Image.Caption import get_caption_from_file
from API.Upload import upload_to_imgbb


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
            self.__caption = get_caption_from_file(self.__path)
        return self.__caption
    
    @property
    def url(self): 
        return self.__url

    def upload(self, api_key):
        self.__url = upload_to_imgbb(api_key, self.path, expire_seconds=120) # expires after 2 minuets 
        
    def delete(self): 
        """
        Removes image from used images
        """
        # not implemented yet!
        pass
    
    def move_on_disK(self, dst):
        dst = validate(dst)
        self.path.replace(dst.joinpath(self.path.name))
            
        
