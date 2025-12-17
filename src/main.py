from Utils.config import parse_config, write_config
from Utils.Timestamp import print_timestamp
from Image.Sample import get_sample 
from Image.Image import Image
from API.Post import Post
from Utils.Token import get_long_lived_token, validate

import sys

if __name__ == "__main__":
    print_timestamp() # print current date and time to console (for logging) 
    
    config = parse_config()

    # retrieve photo
    image_path = get_sample(config["data"]["image_dir"])
    img = Image()
    img.path = image_path
    try: 
        img.caption # load caption
    except: 
        print("Title could not be read from file. Exiting and moving file to corrupted directory...")
        img.move_on_disK(dst= config["data"]["corrupted_image_dir"])
        sys.exit(0)

    img.upload(config["authentication"]["IMGBB_API_KEY"])
    url = img.url
    
    # check if token valid: 
    if not validate(config, TOKEN=config["authentication"]["LONG_LIVED_TOKEN"]): 
        config["authentication"]["LONG_LIVED_TOKEN"] = get_long_lived_token(config) 
        write_config(config)
        # write new code to config
        
    post = Post()
    post.ACCESS_TOKEN = config["authentication"]["LONG_LIVED_TOKEN"]
    post.USER_ID = config["authentication"]["IG_USER_ID"]
    post.post_photo(image_url=url, caption=img.caption)
    
    # delete / move used image 
    if config["settings"]["moveUsedPictures"]: 
        img.move_on_disK(dst= config["data"]["used_image_dir"])
    elif config["settings"]["deleteUsedPictures"]: 
        img.delete()

