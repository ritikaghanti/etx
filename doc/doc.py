import docx2txt

def extract_from_doc(file_path):
    try:
        text = docx2txt.process(file_path)
        fields = {}

        # Simple rules-based extraction (you can customize these)
        lines = text.splitlines()
        for line in lines:
            line = line.strip()
            if line.lower().startswith("name:"):
                fields["name"] = line.split(":", 1)[1].strip()
            elif line.lower().startswith("email:"):
                fields["email"] = line.split(":", 1)[1].strip()
            elif line.lower().startswith("dob:") or line.lower().startswith("date of birth"):
                fields["dob"] = line.split(":", 1)[1].strip()
            elif line.lower().startswith("id:"):
                fields["id"] = line.split(":", 1)[1].strip()
            elif line.lower().startswith("city:"):
                fields["city"] = line.split(":", 1)[1].strip()

        return {
            "raw_text": text,
            **fields
        }

    except Exception as e:
        return {"error": str(e)}
