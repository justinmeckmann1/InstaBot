from path_helper import validate
from caption import get_caption_from_file


class Photo: 
    def __init__(self):
        self.__path = None
        self.__caption = None
        self.__url = None       
        
    
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

    
