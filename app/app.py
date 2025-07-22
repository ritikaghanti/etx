import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from doc.doc import extract_from_doc
from gtts import gTTS
from flask import send_file
from flask import Flask, request, render_template, jsonify
import os
from extract.extract import extract_fields
from doc.doc import extract_from_doc
from transcribe.transcribe import transcribe_audio

from interpret.interpret import interpret_text

app = Flask(__name__)
UPLOAD_FOLDER = os.path.join(os.getcwd(), "uploads")
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Ensure upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/extract_image", methods=["POST"])
def extract_image():
    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"}), 400
    file = request.files["image"]
    if file.filename == "":
        return jsonify({"error": "No selected image"}), 400

    path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(path)
    result = extract_fields(path)
    return jsonify(result)

@app.route("/extract_doc", methods=["POST"])
def extract_doc():
    if "document" not in request.files:
        return jsonify({"error": "No document uploaded"}), 400

    file = request.files["document"]
    if file.filename == "":
        return jsonify({"error": "No selected document"}), 400

    filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(filepath)

    result = extract_from_doc(filepath)
    return jsonify(result)


@app.route("/extract_audio", methods=["POST"])
def extract_audio():
    if "audio" not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files["audio"]
    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(filepath)

    try:
        # Step 1: Transcribe
        text = transcribe_audio(filepath)

        # Step 2: Convert to speech
        tts = gTTS(text)
        audio_response_path = os.path.join(app.config["UPLOAD_FOLDER"], "response.mp3")
        tts.save(audio_response_path)

        # Step 3: Return transcription and audio file path
        return jsonify({
            "transcription": text,
            "audio_reply": "/get_audio_response"
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/get_audio_response")
def get_audio_response():
    audio_path = os.path.join(app.config["UPLOAD_FOLDER"], "response.mp3")
    return send_file(audio_path, mimetype="audio/mpeg")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
