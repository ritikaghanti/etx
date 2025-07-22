from extract.extract import extract_fields

if __name__ == "__main__":
    image_path = "uploads/doc.png"  # Replace with your actual image name
    result = extract_fields(image_path)
    print("✅ Extraction Result:")
    print(result)
