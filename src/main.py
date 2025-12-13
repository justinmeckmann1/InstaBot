from sample import get_sample 

from photo import Photo
from post import Post



if __name__ == "__main__":
    ACCESS_TOKEN = "EAAVNHZCXohmcBQOZCQczoZBRWjkSZBLT8u7vWwwFOsuCDAfiH440RJrILcTLUViz1n2ihNKIBF1gTpLOAZAaQDE7K8OwPeBoNPcN1sID6MIpoqDdeOfSZBfnbShTRNGiRg8Sgtu2NWkuDN7nGskrKOVH77J0zuSVVtiSkE6IzGEBYMocoZAYmy8ZCZAds6DnzuQlmMg9zQJDlUQEo9tuHKZBM9p8OZCRkpEhtM6ZCYXGuVk5Vbia6c6ZAZAp66" 
    IG_USER_ID   = "17841400945712258"  
    
    image_dir = rf"C:\Users\justi\SynologyDrive\InstaBot\post"
    url = rf"https://drive.meckimac.com/d/s/16C54L7sPeI24TzgscVWUx3XpYFLtU6W/webapi/entry.cgi/251123-_DSC9422-Edit.jpg?api=SYNO.SynologyDrive.Files&method=download&version=2&files=%5B%22id%3A923159857165549359%22%5D&force_download=false&sharing_token=%22EoVls4tQHOe795POnJBqzVeEH6dezDf8qZuajLDT93xA6i94eqKw9xPQjVVN0s1JAgGpcFaUXv13tRCP2EwxNsQWfv9fIt0At3i238YYVswPo8jXvuA0N6fVVYEl5jpuPTuubg7F6sxscQJjMDDlUavY6csYux8CVhYfVIq29hLPsQOFCrS8cSJVIJGJXNcTggy.KS3.bJQ8HO82EFs3QbL43PVaI8jX9zumkrf4hHqaHJ0INXpb5S5_%22&_dc=1765573008467" #
    
    image_path = get_sample(image_dir)
    photo = Photo()
    photo.path = image_path
    
    print(photo.caption)
    
    post = Post()
    post.ACCESS_TOKEN = ACCESS_TOKEN
    post.USER_ID = IG_USER_ID
    
    post.post_photo(image_url=url, caption=photo.caption)
        
    # image_url = "https://live.staticflickr.com/65535/54927165362_6e791fe6c0_h.jpg"
    # caption = "Test"
    

    

    # post_photo(ACCESS_TOKEN, IG_USER_ID, image_url, caption)
