from transcriber import transcribe_audio
import ollama

audio_path = input("Enter audio/video file path: ")

print("\nTranscribing audio...\n")

transcript = transcribe_audio(audio_path)

print("\n===== TRANSCRIPT =====\n")
print(transcript)

print("\nGenerating summary\n")

response = ollama.chat(
    model="llama3",
    messages=[
        {
            "role": "user",
            "content": f"""
Summarize the following transcript.

Provide:
1. Executive Summary
2. Key Points
3. Action Items

Transcript:
{transcript}
"""
        }
    ]
)

print("\n== SUMMARY ==\n")
print(response["message"]["content"])