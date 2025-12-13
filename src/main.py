from post import post_photo


if __name__ == "__main__":
    ACCESS_TOKEN = "EAAVNHZCXohmcBQOZCQczoZBRWjkSZBLT8u7vWwwFOsuCDAfiH440RJrILcTLUViz1n2ihNKIBF1gTpLOAZAaQDE7K8OwPeBoNPcN1sID6MIpoqDdeOfSZBfnbShTRNGiRg8Sgtu2NWkuDN7nGskrKOVH77J0zuSVVtiSkE6IzGEBYMocoZAYmy8ZCZAds6DnzuQlmMg9zQJDlUQEo9tuHKZBM9p8OZCRkpEhtM6ZCYXGuVk5Vbia6c6ZAZAp66" 
    IG_USER_ID   = "17841400945712258"  
    image_url = "https://live.staticflickr.com/65535/54927165362_6e791fe6c0_h.jpg"
    caption = "Test"

    post_photo(ACCESS_TOKEN, IG_USER_ID, image_url, caption)
