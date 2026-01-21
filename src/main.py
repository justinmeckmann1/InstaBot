from Utils.config import parse_config, write_config
from Utils.Timestamp import print_timestamp
from Image.Sample import get_sample 
from Image.Image import Image
from API.Post import Post
from Utils.Token import get_long_lived_token, validate

if __name__ == "__main__":
    print_timestamp() # print current date and time to console (for logging) 
    config = parse_config()

    # retrieve photo
    img = Image()
    img.path = get_sample(config["data"]["image_dir"])
    
    # move image to corrupted dir at start. Only move to posted dir if successful 
    img.move_on_disK(dst= config["data"]["corrupted_image_dir"])
    
    try: 
        img.caption # load caption
    except: 
        raise("Title could not be read from file. Exiting and moving file to corrupted directory...")

    img.upload(config["authentication"]["IMGBB_API_KEY"])
    
    # check if token valid: 
    if not validate(config, TOKEN=config["authentication"]["LONG_LIVED_TOKEN"]): 
        config["authentication"]["LONG_LIVED_TOKEN"] = get_long_lived_token(config) 

        # write new code to config
        write_config(config)
    
    # post image to instagram
    
    post = Post()
    post.ACCESS_TOKEN = config["authentication"]["LONG_LIVED_TOKEN"]
    post.USER_ID = config["authentication"]["IG_USER_ID"]
    
    # because we often get time out errors, we will try n times before aborting
    maxAttempts = config["settings"]["maxAttempts"]
    for i in range(1, maxAttempts+1):
        print(f"Try number: {i}")
        try: 
            post.post_photo(image_url=img.url, caption=img.caption)
            
            # move image to used image dir if every thing was successful
            img.move_on_disK(dst= config["data"]["used_image_dir"])
            
            break 

        except: 
            if i == maxAttempts: 
                print("All attempts have failed. Exiting now.")
            else: 
                print(f"Attempt {i}/{maxAttempts} has failed. Trying again...")
            
    
        