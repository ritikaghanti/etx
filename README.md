# 🧠 ETX Modular AI Pipeline

A modular, local-first AI pipeline that accepts audio, document, image, and text inputs to extract structured information using OpenAI’s API. This project is organized for easy extension, local testing, and modular usage.

---

## Watch it here:
[![Watch the demo](uploads/hompepage.png)](https://youtu.be/KTrsqdnbFrk)

Inputs used: 
- [Download Input docx](uploads/Certificate of Distinction - UTA The University of Texas at Arlington &.docx)
- [Download Input png](uploads/doc.png)
- [Download Input audio](uploads/sample.wav)
## 🚀 Features

- 🧾 Document Text Extraction (`docx2txt`)
- 🧠 Intent and Entity Extraction using **OpenAI GPT**
- 🔊 Audio Transcription using **Whisper**
- 📸 Image-to-Text using **Tesseract OCR**
- 🗣️ Text-to-Speech synthesis with **gTTS**
- 🧱 Modular architecture for easy plug-and-play

---

## 📁 Project Structure
```

modular_pipeline/
├── app/ # Main web server
│ └── app.py # Flask app
├── doc/ # Document parsing
│ └── doc.py
├── image/ # Image processing
│ └── image.py
├── transcribe/ # Whisper-based audio transcription
│ └── transcribe.py
├── utils/ # Helper functions (e.g., token counting, logging)
│ └── utils.py
├── static/ # Optional frontend files (HTML, CSS)
│ └── index.html
│
├── render.yaml # Render deployment config
│
├── runtime.txt # Python version lock
│
├── .env # Your local API key (not pushed to GitHub)
│
├── requirements.txt # Python dependencies
│
└── README.md # You are here!
```
## 1. Clone the repository

```bash
git clone https://github.com/ritikaghanti/etx.git
cd etx-modular-pipeline
```

## 2. Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

## 3. Install dependencies
```bash
pip install -r requirements.txt
```

## 4. Set up environment variables
Create a .env file in the root directory:
```env
OPENAI_API_KEY=your_openai_key
```

## 5. Run the application locally

```bash
python app/app.py
```

## 🛠 Dependencies (from requirements.txt)
- Flask

- openai

- docx2txt

- pytesseract

- gTTS

- ffmpeg-python

- numpy

- whisper

- opencv-python

- torch

Make sure ffmpeg and tesseract are installed on your system.

## ⚙️ Tips
Install Tesseract:
``` bash
# On macOS
brew install tesseract
# On Ubuntu
sudo apt-get install tesseract-ocr
```
Install FFmpeg:
```bash
# On macOS
brew install ffmpeg

# On Ubuntu
sudo apt install ffmpeg
```

👩‍💻 Author:  Ritika Ghanti