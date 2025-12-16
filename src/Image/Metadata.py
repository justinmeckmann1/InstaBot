from pathlib import Path
from PIL import Image
from PIL.ExifTags import TAGS
import xml.etree.ElementTree as ET

def _get_xmp_block(image_path: Path) -> str | None:
    with open(image_path, "rb") as f:
        b = f.read()

    start = b.find(b"<x:xmpmeta")
    end = b.find(b"</x:xmpmeta>")
    if start == -1 or end == -1:
        return None

    return b[start:end + len(b"</x:xmpmeta>")].decode("utf-8", errors="ignore")


def _get_xmp_value(root: ET.Element, xpath: str, ns: dict) -> str | None:
    """
    Return XMP value from either:
    - element text: <xmp:CreateDate>...</xmp:CreateDate>
    - attribute on an element: <rdf:Description xmp:CreateDate="..."/>
    """
    el = root.find(xpath, ns)
    if el is not None:
        # Element-text case
        if el.text and el.text.strip():
            return el.text.strip()

        # Attribute case on the found element
        if ":" in xpath:
            _, local = xpath.rsplit(":", 1)
            for k, v in el.attrib.items():
                if k.split("}")[-1] == local and isinstance(v, str) and v.strip():
                    return v.strip()

    # Attribute-only case stored on rdf:Description or similar
    if ":" in xpath:
        prefix, local = xpath.rsplit(":", 1)
        prefix = prefix.split("/")[-1].lstrip(".")
        uri = ns.get(prefix)
        if uri:
            attr_key = f"{{{uri}}}{local}"
            for e in root.iter():
                v = e.attrib.get(attr_key)
                if isinstance(v, str) and v.strip():
                    return v.strip()

    return None



def _get_xmp_field(xmp_xml: str, meta_type: str) -> str | None:
    wanted = meta_type.strip().lower()

    ns = {
        "x": "adobe:ns:meta/",
        "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
        "dc": "http://purl.org/dc/elements/1.1/",
        "photoshop": "http://ns.adobe.com/photoshop/1.0/",
        "xmp": "http://ns.adobe.com/xap/1.0/",
        "exif": "http://ns.adobe.com/exif/1.0/",
        "tiff": "http://ns.adobe.com/tiff/1.0/",
    }

    try:
        root = ET.fromstring(xmp_xml)
    except ET.ParseError:
        return None

    def _read_dc_alt(field: str) -> str | None:
        for li in root.findall(f".//dc:{field}//rdf:li", ns):
            if li.text and li.text.strip():
                return li.text.strip()
        return None

    if wanted == "title":
        return _read_dc_alt("title")

    if wanted in ("subject", "description", "caption"):
        return _read_dc_alt("description")

    if wanted in ("author", "creator", "artist"):
        for li in root.findall(".//dc:creator//rdf:li", ns):
            if li.text and li.text.strip():
                return li.text.strip()
        return None

    if wanted in ("datetaken", "date taken", "originaldatetaken", "original date taken"):
        # Try XMP in a sensible order
        for xp in (
            ".//exif:DateTimeOriginal",
            ".//photoshop:DateCreated",
            ".//xmp:CreateDate",
            ".//xmp:DateTimeOriginal",   # some tools
            ".//tiff:DateTime",
        ):
            v = _get_xmp_value(root, xp, ns)
            if v:
                return v
        return None

    return None


def _exif_get_by_tagname(exif_data, wanted_tagname: str):
    for tag_id, value in exif_data.items():
        if TAGS.get(tag_id, tag_id) == wanted_tagname:
            return value
    return None


def read_metadata(image_path: Path, meta_type: str) -> str | None:
    with Image.open(image_path) as img:
        wanted = meta_type.strip().lower()

        exif_data = img.getexif()

        # Special handling: Windows "Date taken" is NOT an EXIF tag name.
        if wanted in ("datetaken", "date taken", "originaldatetaken", "original date taken"):
            if exif_data:
                v = _exif_get_by_tagname(exif_data, "DateTimeOriginal")
                if v:
                    return v
                v = _exif_get_by_tagname(exif_data, "DateTimeDigitized")
                if v:
                    return v

            # EXIF missing -> try XMP
            xmp_xml = _get_xmp_block(Path(image_path))
            if xmp_xml:
                return _get_xmp_field(xmp_xml, meta_type)

            return None

        # Normal case: match EXIF tag names like "Artist", "Model", "Software", etc.
        if exif_data:
            for tag_id, value in exif_data.items():
                tag_name = TAGS.get(tag_id, tag_id)
                if str(tag_name).lower() == wanted:
                    return value

        # Fallback: XMP for fields like Title
        xmp_xml = _get_xmp_block(Path(image_path))
        if xmp_xml:
            v = _get_xmp_field(xmp_xml, meta_type)
            if v:
                return v

        return None
