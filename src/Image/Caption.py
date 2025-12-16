from Image.Metadata import read_metadata

from datetime import datetime

def get_caption_title_date(title: str, date: str = None): 
    caption = ""
    if title == None: 
        raise("Title could not be read from file. Exiting...")
    else:
        caption += title 
    if not date == None: 
        date = datetime.fromisoformat(date)
        caption += f"\n\n{date.strftime('%B')} {date.day}, {date.year}"
    
    return caption

def get_caption_from_file(file): 
    title = read_metadata(file, meta_type="Title")
    date = read_metadata(file, meta_type="DateTaken")
    return get_caption_title_date(title, date)
    
    