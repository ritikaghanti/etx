import re
from PIL import Image
import pytesseract

def extract_fields(image_path):
    text = pytesseract.image_to_string(Image.open(image_path))

    fields = {
        "raw_text": text.strip(),
        "name": None,
        "dob": None,
        "email": None,
        "id": None,
        "city": None
    }

    # Extract Name
    name_match = re.search(r"(?:Name|name)\s*[:\-]?\s*(.+)", text)
    if name_match:
        fields["name"] = name_match.group(1).strip()

    # Extract DOB (any date-like format)
    dob_match = re.search(r"(?:DOB|dob|Date of Birth)\s*[:\-]?\s*(\d{1,2}[/-]\d{1,2}[/-]\d{2,4})", text)
    if dob_match:
        fields["dob"] = dob_match.group(1).strip()

    # Extract Email
    email_match = re.search(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", text)
    if email_match:
        fields["email"] = email_match.group(0).strip()

    # Extract ID
    id_match = re.search(r"(?:ID|id)\s*[:\-]?\s*(\d+)", text)
    if id_match:
        fields["id"] = id_match.group(1).strip()

    # Extract City
    city_match = re.search(r"(?:City|city)\s*[:\-]?\s*(\w+)", text)
    if city_match:
        fields["city"] = city_match.group(1).strip()

    return fields
