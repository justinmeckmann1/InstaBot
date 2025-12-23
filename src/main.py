from Utils.config import parse_config, write_config
from Utils.Timestamp import print_timestamp
from Image.Sample import get_sample 
from Image.Image import Image
from API.Post import Post
from Utils.Token import get_long_lived_token, validate

import sys
import os 
from pathlib import Path

if __name__ == "__main__":
    print_timestamp() # print current date and time to console (for logging) 
    config = parse_config()

    maxAttempts = config["settings"]["maxAttempts"] if "maxAttempts" in config["settings"] else 5

    for i in range(maxAttempts):
        try: 
            # retrieve photo
            image_path = get_sample(config["data"]["image_dir"])
            img = Image()
            img.path = image_path
            print(f"Image chosen for posting: {img.path.name}")
            print(f"Caption: \n{img.caption}")
            img.upload(api_key=config["authentication"]["IMGBB_API_KEY"])
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

            sys.exit(0)

        except Exception as e:
            # Catch any execption and move the file into the corrupted directory
            print("An error has occured. ")
            try: 
                dst = Path(config["data"]["corrupted_image_dir"])
            except:
                dst = Path("corrupted/")
            if not dst.exists(): 
                os.mkdirs(dst)

    print(f"All {maxAttempts} attempts have failed.")
    sys.exit(1)
