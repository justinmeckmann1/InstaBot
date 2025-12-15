import os
import sys
import time
import requests 

class Post: 
    def __init__(self):
        self.GRAPH = "https://graph.facebook.com/v24.0"
        self.__ACCESS_TOKEN = None
        self.__USER_ID = None
        self.__media_id = None # ID once posted
        

    @property
    def ACCESS_TOKEN(self): 
        return None # this stays private! 

    @ACCESS_TOKEN.setter
    def ACCESS_TOKEN(self, token): 
        self.__ACCESS_TOKEN = token
        

    @property
    def USER_ID(self): 
        return self.__USER_ID

    @USER_ID.setter
    def USER_ID(self, id): 
        self.__USER_ID = id
    

    def die(self, msg: str):
        print(msg, file=sys.stderr)
        sys.exit(1)

    def post_photo(self, image_url: str, caption: str = "") -> str:
        if not self.__ACCESS_TOKEN or not self.__USER_ID:
            self.die("Set env vars ACCESS_TOKEN and IG_USER_ID first.")

        # 1) Create container
        r = requests.post(
            f"{self.GRAPH}/{self.__USER_ID}/media",
            data={
                "image_url": image_url,
                "caption": caption,
                "access_token": self.__ACCESS_TOKEN,
            },
            timeout=30,
        )
        data = r.json()
        if r.status_code != 200:
            self.die(f"Create container failed: {data}")
        creation_id = data["id"]
        print("creation_id:", creation_id)

        # Optional: wait a moment (usually not needed, but avoids occasional race)
        time.sleep(2)

        # 2) Publish container
        r = requests.post(
            f"{self.GRAPH}/{self.__USER_ID}/media_publish",
            data={
                "creation_id": creation_id,
                "access_token": self.__ACCESS_TOKEN,
            },
            timeout=30,
        )
        data = r.json()
        if r.status_code != 200:
            self.die(f"Publish failed: {data}")

        self.__media_id = data["id"]
        print("media_id:", self.__media_id)
        return self.__media_id


