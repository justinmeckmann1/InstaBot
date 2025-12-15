from Image.Compress import compress

import requests
from pathlib import Path
from pathlib import Path

def upload_to_imgbb(api_key, image_path: str, expire_seconds: int = 600) -> str:
    print("Uploading image...")

    image_path = Path(image_path)

    # recompress if needed
    if image_path.stat().st_size > 8 * 1024 * 1024:
        image_bytes = compress(str(image_path))
        files = {"image": ("image.jpg", image_bytes)}
    else:
        files = {"image": open(image_path, "rb")}

    url = "https://api.imgbb.com/1/upload"

    r = requests.post(
        url,
        params={
            "key": api_key,
            "expiration": expire_seconds,
        },
        files=files,
        timeout=30,
    )

    r.raise_for_status()
    data = r.json()

    if not data.get("success"):
        raise RuntimeError(data)

    image_url = data["data"]["url"]
    print(f"Uploaded image to {image_url}.\nExpires in {expire_seconds} seconds.")

    return image_url


