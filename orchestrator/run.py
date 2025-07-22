import sys
import os
import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from transcribe.transcribe import transcribe_audio
from interpret.interpret import interpret_text
from synthesize.synthesize import synthesize_speech
from extract.extract import extract_fields

def process(file_path):
    ext = os.path.splitext(file_path)[1].lower()
    output = {}

    if ext in ['.wav', '.mp3']:
        print("[INFO] Processing audio...")
        text = transcribe_audio(file_path)
        print("[INFO] Transcribed:", text)
        intent = interpret_text(text)
        print("[INFO] Intent:", intent)
        synthesize_speech(f"You said: {text}")
        output = {"transcription": text, "intent": intent}

    elif ext in ['.png', '.jpg', '.jpeg']:
        print("[INFO] Processing image...")
        fields = extract_fields(file_path)
        print("[INFO] Fields:", fields)
        output = fields

    else:
        print("[ERROR] Unsupported file type.")
        return

    json.dump(output, open("output.json", "w"), indent=2)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        process(sys.argv[1])
    else:
        print("Usage: python -m orchestrator.run <file_path>")
