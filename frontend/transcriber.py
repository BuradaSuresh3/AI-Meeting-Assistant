import os
import whisper

os.environ["PATH"] += os.pathsep + r"C:\Users\User\Downloads\ffmpeg-8.1.1-essentials_build\ffmpeg-8.1.1-essentials_build\bin"

print("Loading Whisper model...")

model = whisper.load_model("base")

print("Model loaded successfully!")

def transcribe_audio(file_path):
    result = model.transcribe(
        file_path,
        fp16=False
    )

    return result["text"]