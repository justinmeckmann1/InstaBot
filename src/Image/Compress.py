from PIL import Image
import io

def compress(src: str, MAX_SIZE = 8 * 1024 * 1024) -> bytes:
    img = Image.open(src).convert("RGB")

    quality = 95
    while quality >= 70:
        buf = io.BytesIO()
        img.save(buf, format="JPEG", quality=quality, optimize=True)
        if buf.tell() <= MAX_SIZE:
            return buf.getvalue()
        quality -= 5

    raise RuntimeError("Image cannot be compressed under 8 MB by quality alone")