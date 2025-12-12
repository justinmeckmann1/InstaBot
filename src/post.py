# post_instagram_photo.py
import os
import sys
import time
import requests
   # your Instagram Business/Creator IG user id

GRAPH = "https://graph.facebook.com/v24.0"


def die(msg: str):
    print(msg, file=sys.stderr)
    sys.exit(1)

def post_photo(image_url: str, caption: str = "") -> str:
    if not ACCESS_TOKEN or not IG_USER_ID:
        die("Set env vars IG_ACCESS_TOKEN and IG_USER_ID first.")

    # 1) Create container
    r = requests.post(
        f"{GRAPH}/{IG_USER_ID}/media",
        data={
            "image_url": image_url,
            "caption": caption,
            "access_token": ACCESS_TOKEN,
        },
        timeout=30,
    )
    data = r.json()
    if r.status_code != 200:
        die(f"Create container failed: {data}")
    creation_id = data["id"]
    print("creation_id:", creation_id)

    # Optional: wait a moment (usually not needed, but avoids occasional race)
    time.sleep(2)

    # 2) Publish container
    r = requests.post(
        f"{GRAPH}/{IG_USER_ID}/media_publish",
        data={
            "creation_id": creation_id,
            "access_token": ACCESS_TOKEN,
        },
        timeout=30,
    )
    data = r.json()
    if r.status_code != 200:
        die(f"Publish failed: {data}")

    media_id = data["id"]
    print("media_id:", media_id)
    return media_id

if __name__ == "__main__":
    # Example usage:
    # export IG_ACCESS_TOKEN="EAAB..."
    # export IG_USER_ID="1789..."
    # python post_instagram_photo.py "https://yourdomain.com/public/test.jpg" "hello from python"

    # if len(sys.argv) < 2:
    #     die("Usage: python post_instagram_photo.py <public_image_https_url> [caption]")
    image_url = "https://live.staticflickr.com/65535/54927165362_6e791fe6c0_h.jpg"
    caption = "Test"
    post_photo(image_url, caption)
