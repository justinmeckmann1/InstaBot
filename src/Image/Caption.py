from Image.Metadata import get_metadata

from datetime import datetime

def get_caption(title: str, date: str = None): 
    caption = ""
    if not title == None: #TODO --> if loop keeps program from crashing. But we do not want pictures without a caption!
        caption += title 
    if not date == None: 
        date = datetime.fromisoformat(date)
        caption += f"\n\n{date.strftime('%B')} {date.day}, {date.year}"
    
    return caption

def get_caption_from_file(file): 
    title = get_metadata(file, meta_type="Title")
    date = get_metadata(file, meta_type="DateTaken")
    
    return get_caption(title, date)
    
    