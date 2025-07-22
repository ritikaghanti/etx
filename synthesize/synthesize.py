from gtts import gTTS
import os

def synthesize_speech(text):
    tts = gTTS(text)
    output_path = os.path.join(os.path.dirname(__file__), "..", "response.wav")
    tts.save(output_path)
